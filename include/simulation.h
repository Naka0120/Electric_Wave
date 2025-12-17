#ifndef SIMULATION_H
#define SIMULATION_H

#include <vector>

const int Nx = 400; // Number of spatial points
const double dx = 0.01; // Spatial step size
const double dt = 0.005; // Time step size
const double c = 299792458; // Speed of light in vacuum

// Arrays to hold the electric and magnetic fields
extern std::vector<double> ey; // Electric field
extern std::vector<double> bz; // Magnetic field

// Function declarations
void initializeFields();
void updateFields();
void applyBoundaryConditions();

#endif // SIMULATION_H