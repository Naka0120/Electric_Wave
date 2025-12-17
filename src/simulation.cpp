#include "simulation.h"
#include <cmath>
#include <vector>

const int Nx = 400; // Number of spatial points
const double dt = 0.01; // Time step
const double dx = 0.1; // Spatial step
const double c = 1.0; // Speed of light in vacuum

std::vector<double> ey(Nx, 0.0); // Electric field array
std::vector<double> bz(Nx, 0.0); // Magnetic field array

void initialize_fields() {
    for (int i = 0; i < Nx; ++i) {
        ey[i] = 0.0;
        bz[i] = 0.0;
    }
}

void update_fields() {
    // Update magnetic field bz based on the electric field ey
    for (int i = 0; i < Nx - 1; ++i) {
        bz[i] += (dt / (dx * 1.0)) * (ey[i + 1] - ey[i]);
    }

    // Update electric field ey based on the magnetic field bz
    for (int i = 1; i < Nx; ++i) {
        ey[i] += (dt / (dx * 1.0)) * (bz[i] - bz[i - 1]);
    }

    // Apply boundary conditions
    ey[0] = 0.0; // Boundary condition at the left end
    ey[Nx - 1] = 0.0; // Boundary condition at the right end
}

void simulate(int steps) {
    initialize_fields();
    for (int t = 0; t < steps; ++t) {
        update_fields();
    }
}