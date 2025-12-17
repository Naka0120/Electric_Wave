# One-Dimensional Electromagnetic Wave Simulation

This project simulates the propagation of electromagnetic waves in one dimension. It implements the basic equations of electromagnetism to model the behavior of electric and magnetic fields over time. The simulation includes visualization capabilities to observe the wave propagation.

## Project Structure

- **src/**: Contains the source code files for the simulation.
  - `main.cpp`: Entry point of the simulation program.
  - `simulation.cpp`: Implements the simulation logic, including field updates.
  - `visualization.cpp`: Handles the visualization of the simulation results.
  - `boundary_conditions.cpp`: Implements boundary conditions for the simulation.

- **include/**: Contains header files for the simulation.
  - `simulation.h`: Declares functions and constants for the simulation.
  - `visualization.h`: Declares visualization functions.
  - `boundary_conditions.h`: Declares functions for boundary conditions.

- **tests/**: Contains unit tests for the simulation functions.
  - `test_simulation.cpp`: Tests the update logic and boundary conditions.

- **examples/**: Contains example configuration files for running the simulation.
  - `example_config.json`: Provides example parameters for the simulation.

- **scripts/**: Contains scripts for building and running the project.
  - `build.sh`: Automates the build process.
  - `run.sh`: Runs the compiled simulation program.

- **CMakeLists.txt**: Configuration file for CMake, specifying project structure and build instructions.

- **.gitignore**: Specifies files and directories to be ignored by Git.

## Building the Project

To build the project, navigate to the project directory and run the following command:

```bash
./scripts/build.sh
```

This will compile the source files and create an executable for the simulation.

## Running the Simulation

After building the project, you can run the simulation using the following command:

```bash
./scripts/run.sh
```

You may specify a configuration file to customize the simulation parameters.

## Visualization

The simulation includes visualization of the electric and magnetic fields over time. Ensure you have the necessary libraries installed for graphical output.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.