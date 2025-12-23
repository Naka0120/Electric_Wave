import numpy as np
import matplotlib.pyplot as plt
from em_1d_sim import EMSimulation1D

def verify_and_plot():
    # --- Simulation Setup ---
    nx = 400
    dx = 1.0
    c = 10.0
    eps0 = 1.0
    dt_ratio = 0.5
    
    sim = EMSimulation1D(nx, dx, c, eps0, dt_ratio=dt_ratio)
    
    # Target Parameters (From Slide)
    omega = 5.0
    freq = omega / (2 * np.pi)
    target_period = 1.0 / freq
    target_lambda = c / freq
    
    # Run Simulation
    steps = 600
    source_pos = nx // 2
    probe_pos = source_pos + 50 # Measure 50 units away from source
    
    probe_signal = []
    time_history = []
    
    print(f"Running simulation for {steps} steps...")
    
    for _ in range(steps):
        # Continuous sinusoidal source J0 * sin(omega * t)
        current = np.sin(omega * sim.t)
        sim.update(source_current=current, source_pos_idx=source_pos)
        
        probe_signal.append(sim.ey[probe_pos])
        time_history.append(sim.t)

    # --- Analysis ---
    
    # 1. Temporal Analysis (Period)
    # Use the last 50% of signal to ensure steady state
    start_idx = int(len(probe_signal) * 0.5)
    t_data = np.array(time_history)[start_idx:]
    y_time_data = np.array(probe_signal)[start_idx:]
    
    # Find peaks in time
    peaks_t_idx = []
    for i in range(1, len(y_time_data)-1):
        if y_time_data[i-1] < y_time_data[i] and y_time_data[i] > y_time_data[i+1]:
            peaks_t_idx.append(i)
            
    measured_period = 0.0
    if len(peaks_t_idx) >= 2:
        diffs = np.diff(t_data[peaks_t_idx])
        measured_period = np.mean(diffs)
    
    # 2. Spatial Analysis (Wavelength)
    # Snapshot at final step
    x_data = np.arange(nx+1) * dx
    y_space_data = sim.ey
    
    # Look at the right side of the source to avoid interference with left wave
    # Source is at 200. Let's look at 220 to 380
    region_mask = (x_data > (source_pos * dx + 20)) & (x_data < (nx * dx - 20))
    x_region = x_data[region_mask]
    y_region = y_space_data[region_mask]
    
    peaks_x_idx = []
    for i in range(1, len(y_region)-1):
        if y_region[i-1] < y_region[i] and y_region[i] > y_region[i+1]:
            peaks_x_idx.append(i)
            
    measured_lambda = 0.0
    if len(peaks_x_idx) >= 2:
        diffs = np.diff(x_region[peaks_x_idx])
        measured_lambda = np.mean(diffs)
        
    measured_velocity = measured_lambda / measured_period if measured_period > 0 else 0
    
    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    plt.subplots_adjust(hspace=0.4)
    
    # subplot 1: Time Domain
    ax1.plot(t_data, y_time_data, 'b-', label='Ey at x=250')
    ax1.set_title(f'Temporal Check (Period)\nTarget T={target_period:.2f}, Measured T={measured_period:.4f}')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude')
    ax1.grid(True)
    
    # Mark peaks
    if len(peaks_t_idx) >= 2:
        p1 = peaks_t_idx[-2]
        p2 = peaks_t_idx[-1]
        t1, t2 = t_data[p1], t_data[p2]
        v1, v2 = y_time_data[p1], y_time_data[p2]
        
        ax1.plot([t1, t2], [v1, v2], 'ro')
        ax1.annotate('', xy=(t1, v1 + 0.1), xytext=(t2, v2 + 0.1),
                     arrowprops=dict(arrowstyle='<->', color='red'))
        ax1.text((t1+t2)/2, v1 + 0.2, f'T ~ {t2-t1:.2f}', color='red', ha='center')

    # subplot 2: Spatial Domain
    ax2.plot(x_data, y_space_data, 'g-', label=f'Ey at t={sim.t:.2f}')
    ax2.set_xlim(200, 400) # Zoom in on right side
    ax2.set_title(f'Spatial Check (Wavelength)\nTarget Lambda={target_lambda:.2f}, Measured Lambda={measured_lambda:.4f}')
    ax2.set_xlabel('Position (x)')
    ax2.set_ylabel('Amplitude')
    ax2.grid(True)
    
    # Mark peaks
    if len(peaks_x_idx) >= 2:
        p1 = peaks_x_idx[-2]
        p2 = peaks_x_idx[-1]
        x1, x2 = x_region[p1], x_region[p2]
        v1, v2 = y_region[p1], y_region[p2]
        
        ax2.plot([x1, x2], [v1, v2], 'ro')
        ax2.annotate('', xy=(x1, v1 + 0.1), xytext=(x2, v2 + 0.1),
                     arrowprops=dict(arrowstyle='<->', color='red'))
        ax2.text((x1+x2)/2, v1 + 0.2, f'L ~ {x2-x1:.2f}', color='red', ha='center')

    # Add velocity text
    plt.figtext(0.5, 0.02, 
                f"Calculated Velocity = Lambda / Period = {measured_lambda:.4f} / {measured_period:.4f} = {measured_velocity:.4f}\n"
                f"(Simulation Setting c = {c})", 
                ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})
    
    output_path = 'verification_plot.png'
    plt.savefig(output_path)
    print(f"Saved verification plot to {output_path}")

if __name__ == "__main__":
    verify_and_plot()
