#!/bin/bash

# This script automates the build process for the one-dimensional electromagnetic wave simulation project.

# Create a build directory if it doesn't exist
mkdir -p build
cd build

# Run CMake to configure the project
cmake ..

# Build the project
make

# Return to the original directory
cd ..