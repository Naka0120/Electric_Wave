import numpy as np
import matplotlib.pyplot as plt
import os

class EMSimulation1D:
    def __init__(self, nx, dx, c, eps0, dt_ratio=0.5):
        """
        Initialize the 1D FDTD Simulation.
        
        Args:
            nx (int): Number of grid points.
            dx (float): Grid spacing.
            c (float): Speed of light.
            eps0 (float): Permittivity of free space.
            dt_ratio (float): Ratio of dt to (dx/c). Should be < 1.0 for stability.
        """
        self.nx = nx
        self.dx = dx
        self.c = c
        self.eps0 = eps0
        
        # Stability Condition (CFL)
        # c * dt < dx
        self.dt_limit = dx / c
        self.dt = self.dt_limit * dt_ratio
        
        print(f"[Init] dx={dx}, c={c}, dt_limit={self.dt_limit}, dt={self.dt}")
        if self.dt >= self.dt_limit:
            print("WARNING: Unstable Time Step!")
            
        # Field Arrays
        # Ey is defined at integer steps k (0 to Nx). Size: Nx + 1
        # Bz is defined at half steps k+0.5 (0 to Nx-1). Size: Nx
        self.ey = np.zeros(nx + 1)
        self.bz = np.zeros(nx)
        
        # Time
        self.t = 0.0
        self.step = 0
        
        # Monitoring
        self.history_ey_center = []
        self.history_ey_probe = [] # probe at center + distance
        self.time_history = []

    def update(self, source_current=0.0, source_pos_idx=None):
        """
        Update fields by one time step using Leapfrog method.
        """
        
        # Update Bz (Faraday's Law)
        # dBz/dt = -dEy/dx
        # Bz[k+1/2] (new) = Bz[k+1/2] (old) - (dt/dx) * (Ey[k+1] - Ey[k])
        self.bz[:] -= (self.dt / self.dx) * (self.ey[1:] - self.ey[:-1])
        
        # Update Ey (Ampere's Law)
        # dEy/dt = -c^2 * dBz/dx - J/eps0
        # Ey[k] (new) = Ey[k] (old) - c^2 * (dt/dx) * (Bz[k+1/2] - Bz[k-1/2]) - (dt/eps0)*J
        # Range: 1 to Nx-1 (Internal points). 0 and Nx are boundaries.
        self.ey[1:-1] -= (self.c**2 * self.dt / self.dx) * (self.bz[1:] - self.bz[:-1])
        
        # Apply Source (Current Injection)
        if source_pos_idx is not None:
            # Add Current Density J
            # Note: The source is added to the update equation.
            # J is current density.
            # We assume the source is at a single node.
            self.ey[source_pos_idx] -= (self.dt / self.eps0) * source_current

        # Boundary Conditions (PEC / Metal)
        # Ey = 0 at x=0 and x=Nx*dx
        self.ey[0] = 0.0
        self.ey[-1] = 0.0
        
        # Record history for analysis
        self.time_history.append(self.t)
        if self.history_ey_center is not None and source_pos_idx is not None:
             self.history_ey_center.append(self.ey[source_pos_idx])
        
        # Advance time
        self.t += self.dt
        self.step += 1

def run_simulation(nx=400, dx=1.0, c=10.0, eps0=1.0, dt_ratio=0.5, steps=1000, output_dir="results"):
    """
    Run the simulation and generate plots.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    sim = EMSimulation1D(nx, dx, c, eps0, dt_ratio=dt_ratio)
    
    # Source Parameters
    # Slide example: omega = 5.0
    omega = 5.0
    freq = omega / (2 * np.pi)
    period = 1.0 / freq
    wavelength = c / freq
    
    print(f"Goal: Omega={omega}, Frequency={freq:.4f}, Period={period:.4f}, Wavelength={wavelength:.4f}")
    
    source_pos = nx // 2
    
    # Store snapshots
    snapshots = []
    snapshot_times = []
    
    probe_idx = source_pos + 50 # Point to measure propagation speed
    probe_signal = []
    
    for s in range(steps):
        # Sinusoidal Source: J0 * sin(omega * t)
        # t is simulation time (s * dt)
        current = np.sin(omega * sim.t)
        
        sim.update(source_current=current, source_pos_idx=source_pos)
        
        probe_signal.append(sim.ey[probe_idx])
        
        # Take snapshots at intervals
        if s % 100 == 0:
            snapshots.append((sim.t, sim.ey.copy(), sim.bz.copy()))
            snapshot_times.append(sim.t)

    # --- Visualization ---
    
    # 1. Plot Snapshots of Ey
    plt.figure(figsize=(10, 6))
    for t_val, ey_data, _ in snapshots[::2]: # Plot every 2nd snapshot for clarity
        plt.plot(np.arange(nx+1)*dx, ey_data, label=f"t={t_val:.2f}")
    plt.title(f"Ey Propagation (dt_ratio={dt_ratio})")
    plt.xlabel("Position x")
    plt.ylabel("Ey")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{output_dir}/ey_propagation_dt{dt_ratio}.png")
    plt.close()

    # 2. Verification of Speed, Wavelength, Period
    # We use the probe signal to measure period
    # Find peaks in probe signal
    # Simple peak finding logic
    # Filter only the steady part (latter half)
    signal_slice = np.array(probe_signal)[-int(steps/2):]
    time_slice = np.array(sim.time_history)[-int(steps/2):]
    
    # Zero crossings (Positive slope)
    zero_crossings = np.where(np.diff(np.sign(signal_slice)) > 0)[0]
    
    measured_period = 0.0
    if len(zero_crossings) > 1:
        periods = []
        for i in range(len(zero_crossings)-1):
            t1 = time_slice[zero_crossings[i]]
            t2 = time_slice[zero_crossings[i+1]]
            periods.append(t2 - t1)
        measured_period = np.mean(periods)
    
    measured_freq = 1.0 / measured_period if measured_period > 0 else 0
    measured_wavelength = c / measured_freq if measured_freq > 0 else 0 # Assuming c is correct
    
    # Measure Velocity?
    # Delay between source and probe
    # Harder with continuous wave.
    # Wavelength check directly from spatial snapshot
    # Take last snapshot
    last_t, last_ey, last_bz = snapshots[-1]
    # Find spatial peaks
    # Center is source. Look at right side.
    right_side_ey = last_ey[source_pos:nx]
    spatial_peaks = []
    for i in range(1, len(right_side_ey)-1):
        if right_side_ey[i] > right_side_ey[i-1] and right_side_ey[i] > right_side_ey[i+1]:
            spatial_peaks.append(i * dx) # relative position
    
    measured_lambda_spatial = 0.0
    if len(spatial_peaks) > 1:
        measured_lambda_spatial = np.mean(np.diff(spatial_peaks))
    
    velocity_check = measured_lambda_spatial / measured_period if measured_period > 0 else 0
    
    print(f"--- Verification (dt={dt_ratio}) ---")
    print(f"Set C={c}, Set Period={period:.4f}, Set Wavelength={wavelength:.4f}")
    print(f"Measured Period={measured_period:.4f}")
    print(f"Measured Wavelength (Spatial)={measured_lambda_spatial:.4f}")
    print(f"Calculated Velocity (Lambda/Period)={velocity_check:.4f}")
    
    # Save verification text
    with open(f"{output_dir}/verification_dt{dt_ratio}.txt", "w") as f:
        f.write(f"Parameters: c={c}, dx={dx}, dt={sim.dt}\n")
        f.write(f"Target: Period={period}, Wavelength={wavelength}\n")
        f.write(f"Measured: Period={measured_period}\n")
        f.write(f"Measured: Wavelength={measured_lambda_spatial}\n")
        f.write(f"Measured: Velocity={velocity_check}\n")

if __name__ == "__main__":
    print("Running Stable Simulation (dt_ratio=0.5)...")
    run_simulation(dt_ratio=0.5, output_dir="results_stable")
    
    print("\nRunning Unstable Simulation (dt_ratio=1.01)...")
    # c*dt > dx => dt > dx/c. dt_ratio > 1.0
    try:
        run_simulation(dt_ratio=1.01, steps=200, output_dir="results_unstable")
    except Exception as e:
        print(f"Simulation crashed as expected or produced garbage: {e}")

