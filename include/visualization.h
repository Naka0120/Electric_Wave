#ifndef VISUALIZATION_H
#define VISUALIZATION_H

#include <vector>

// Function to plot the electric field over time
void plotElectricField(const std::vector<double>& ey, int timeStep);

// Function to plot the magnetic field over time
void plotMagneticField(const std::vector<double>& bz, int timeStep);

// Function to initialize the visualization settings
void initializeVisualization();

#endif // VISUALIZATION_H