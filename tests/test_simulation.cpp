#include <gtest/gtest.h>
#include "../src/simulation.h"
#include "../src/boundary_conditions.h"

TEST(SimulationTest, UpdateFields) {
    const int Nx = 400;
    double ey[Nx] = {0};
    double bz[Nx] = {0};

    // Initialize fields for testing
    for (int i = 0; i < Nx; ++i) {
        ey[i] = sin(2 * M_PI * i / Nx);
        bz[i] = cos(2 * M_PI * i / Nx);
    }

    // Update fields
    updateFields(ey, bz, Nx);

    // Check boundary conditions
    EXPECT_DOUBLE_EQ(ey[0], 0);
    EXPECT_DOUBLE_EQ(ey[Nx - 1], 0);

    // Check some internal values (example checks)
    EXPECT_NEAR(ey[Nx / 2], sin(2 * M_PI * (Nx / 2) / Nx), 0.01);
    EXPECT_NEAR(bz[Nx / 2], cos(2 * M_PI * (Nx / 2) / Nx), 0.01);
}

TEST(BoundaryConditionsTest, ApplyBoundaryConditions) {
    const int Nx = 400;
    double ey[Nx] = {1.0}; // Initialize with non-zero values

    applyBoundaryConditions(ey, Nx);

    EXPECT_DOUBLE_EQ(ey[0], 0);
    EXPECT_DOUBLE_EQ(ey[Nx - 1], 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}