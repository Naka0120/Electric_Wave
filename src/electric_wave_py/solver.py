class Solver:
    def __init__(self, nx, dt, c):
        self.nx = nx
        self.dt = dt
        self.c = c
        self.ey = np.zeros(nx)
        self.bz = np.zeros(nx)

    def update_fields(self):
        ey_new = np.copy(self.ey)
        bz_new = np.copy(self.bz)

        for i in range(1, self.nx - 1):
            ey_new[i] = self.ey[i] - (self.c * self.dt / (2 * self.dx)) * (self.bz[i + 1] - self.bz[i - 1])
            bz_new[i] = self.bz[i] - (self.c * self.dt / (2 * self.dx)) * (self.ey[i + 1] - self.ey[i - 1])

        self.ey = ey_new
        self.bz = bz_new

    def set_initial_conditions(self, initial_ey, initial_bz):
        self.ey = initial_ey
        self.bz = initial_bz

    def get_fields(self):
        return self.ey, self.bz