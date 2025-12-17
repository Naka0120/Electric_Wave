#include "boundary_conditions.h"

void applyBoundaryConditions(double* ey, int Nx) {
    ey[0] = 0.0;       // Set the electric field at the left boundary to zero
    ey[Nx - 1] = 0.0;  // Set the electric field at the right boundary to zero
}