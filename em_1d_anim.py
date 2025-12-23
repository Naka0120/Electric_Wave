import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from em_1d_sim import EMSimulation1D

def create_animation():
    # Simulation Parameters
    nx = 400
    dx = 1.0
    c = 10.0
    eps0 = 1.0
    dt_ratio = 0.5
    
    sim = EMSimulation1D(nx, dx, c, eps0, dt_ratio=dt_ratio)
    
    # Source Parameters
    omega = 5.0
    freq = omega / (2 * np.pi)
    source_pos = nx // 2
    
    # Animation Setup
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot([], [], lw=2)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    
    ax.set_xlim(0, nx*dx)
    ax.set_ylim(-1.5, 1.5) # E field usually bounded around +/- 1 with this source, maybe higher?
    # Source is sin(..). dEy/dt ~ J. Ey accumulates?
    # No, dEy/dt = ... - J/eps0.
    # If J is sin(wt), Ey will be cos(wt). Amplitude depends on factors.
    # Let's run a bit to check amplitude range or set ylim dynamically (auto scale is risky for animation).
    # Based on experience, it might grow if resonance, but here it's open radiation.
    # Let's start with generous limits.
    ax.set_ylim(-5.0, 5.0) 
    
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Electric Field Ey')
    ax.set_title('1D EM Wave Propagation (FDTD)')
    ax.grid(True)
    
    # Add Metal Walls indicators
    ax.axvline(0, color='k', linewidth=5, label='PEC Wall')
    ax.axvline(nx*dx, color='k', linewidth=5)
    
    # Total Frames
    frames = 600
    steps_per_frame = 2 # Speed up animation
    
    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text
    
    def animate(i):
        # Advance simulation
        for _ in range(steps_per_frame):
            current = 5.0 * np.sin(omega * sim.t) # Amplitude 5.0 source
            sim.update(source_current=current, source_pos_idx=source_pos)
        
        # Update Plot
        x_data = np.arange(nx+1) * dx
        y_data = sim.ey
        line.set_data(x_data, y_data)
        time_text.set_text(f'Time = {sim.t:.2f}')
        
        return line, time_text
    
    print("Generating animation...")
    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=frames, interval=30, blit=True)
    
    # Save as GIF
    output_file = 'em_wave_animation.gif'
    writer = animation.PillowWriter(fps=30)
    ani.save(output_file, writer=writer)
    print(f"Animation saved to {output_file}")

if __name__ == "__main__":
    create_animation()
