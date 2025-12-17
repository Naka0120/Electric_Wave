class BoundaryConditions:
    def __init__(self, size):
        self.size = size

    def apply(self, ey):
        ey[0] = 0  # Boundary condition at the left end
        ey[self.size - 1] = 0  # Boundary condition at the right end
        return ey