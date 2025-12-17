class Simulation:
    def __init__(self, length=400, time_steps=100, dx=1, dt=0.01):
        self.length = length
        self.time_steps = time_steps
        self.dx = dx
        self.dt = dt
        self.ey = self.initialize_field()
        self.bz = self.initialize_field()

    def initialize_field(self):
        return [0.0] * (self.length // self.dx)

    def update_fields(self):
        for t in range(self.time_steps):
            self.apply_boundary_conditions()
            self.solve_wave_equations()

    def apply_boundary_conditions(self):
        self.ey[0] = 0
        self.ey[-1] = 0

    def solve_wave_equations(self):
        # Implement the finite difference method to update ey and bz
        new_ey = self.ey[:]
        new_bz = self.bz[:]
        
        for i in range(1, len(self.ey) - 1):
            new_ey[i] = self.ey[i] - (self.dt / self.dx) * (self.bz[i] - self.bz[i - 1])
            new_bz[i] = self.bz[i] - (self.dt / self.dx) * (self.ey[i] - self.ey[i - 1])
        
        self.ey = new_ey
        self.bz = new_bz

    def run(self):
        self.update_fields()