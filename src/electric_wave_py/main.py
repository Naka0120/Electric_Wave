# filepath: electric_wave_py/src/electric_wave_py/main.py

import numpy as np
from electric_wave_py.simulation import Simulation
from electric_wave_py.visualization import Visualization

def main():
    # Simulation parameters
    length = 400  # Length of the simulation domain
    time_steps = 200  # Number of time steps
    dx = 1.0  # Spatial step size
    dt = 0.1  # Time step size

    # Initialize the simulation
    simulation = Simulation(length, time_steps, dx, dt)

    # Run the simulation
    simulation.run()

    # Visualize the results
    visualization = Visualization(simulation)
    visualization.plot_fields()

if __name__ == "__main__":
    main()