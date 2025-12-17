# filepath: electric_wave_py/examples/run_simulation.py

import numpy as np
import matplotlib.pyplot as plt
from src.electric_wave_py.main import run_simulation

def main():
    # Set simulation parameters
    duration = 10.0  # seconds
    space_steps = 400
    time_steps = 1000
    c = 3e8  # speed of light in vacuum

    # Run the simulation
    ey, bz, time = run_simulation(duration, space_steps, time_steps, c)

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.title('Electric Field (Ey)')
    plt.imshow(ey, aspect='auto', extent=[0, duration, 0, space_steps], origin='lower')
    plt.colorbar(label='Ey')
    plt.ylabel('Space Steps')
    
    plt.subplot(2, 1, 2)
    plt.title('Magnetic Field (Bz)')
    plt.imshow(bz, aspect='auto', extent=[0, duration, 0, space_steps], origin='lower')
    plt.colorbar(label='Bz')
    plt.xlabel('Time (s)')
    plt.ylabel('Space Steps')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()