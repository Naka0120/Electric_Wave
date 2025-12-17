#include <iostream>
#include "simulation.h"
#include "visualization.h"
#include "boundary_conditions.h"

int main() {
    const int Nx = 400; // Number of spatial points
    const double dx = 0.01; // Spatial step size
    const double dt = 0.01; // Time step size
    const int totalTimeSteps = 1000; // Total number of time steps

    // Initialize electric and magnetic fields
    double ey[Nx] = {0.0};
    double bz[Nx] = {0.0};

    // Set initial conditions (e.g., a Gaussian pulse)
    for (int i = 0; i < Nx; ++i) {
        ey[i] = exp(-0.5 * pow((i - Nx / 2) * dx, 2));
    }

    // Simulation loop
    for (int t = 0; t < totalTimeSteps; ++t) {
        updateFields(ey, bz, Nx, dx, dt);
        applyBoundaryConditions(ey, Nx);
        visualizeFields(ey, bz, Nx, t);
    }

    return 0;
}