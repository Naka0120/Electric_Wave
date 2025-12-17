class Visualization:
    def __init__(self):
        import matplotlib.pyplot as plt
        self.plt = plt

    def plot_fields(self, ey, bz, time_step):
        self.plt.figure(figsize=(12, 6))

        self.plt.subplot(1, 2, 1)
        self.plt.title(f'Electric Field (ey) at t={time_step}')
        self.plt.plot(ey, color='blue')
        self.plt.xlabel('Position')
        self.plt.ylabel('Electric Field (ey)')
        self.plt.grid()

        self.plt.subplot(1, 2, 2)
        self.plt.title(f'Magnetic Field (bz) at t={time_step}')
        self.plt.plot(bz, color='red')
        self.plt.xlabel('Position')
        self.plt.ylabel('Magnetic Field (bz)')
        self.plt.grid()

        self.plt.tight_layout()
        self.plt.show()