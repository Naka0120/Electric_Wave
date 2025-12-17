import unittest
from src.electric_wave_py.visualization import Visualization

class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.visualization = Visualization()

    def test_plot_fields(self):
        # Assuming the Visualization class has a method plot_fields
        # that takes electric and magnetic field data as input
        ey = [0, 1, 0, -1, 0]  # Example electric field data
        bz = [0, 0, 1, 0, -1]  # Example magnetic field data
        result = self.visualization.plot_fields(ey, bz)
        self.assertIsNone(result)  # Assuming the method returns None

    def test_save_plot(self):
        # Assuming the Visualization class has a method save_plot
        filename = "test_plot.png"
        self.visualization.save_plot(filename)
        # Check if the file was created (this is a simple check)
        import os
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)  # Clean up after test

if __name__ == '__main__':
    unittest.main()