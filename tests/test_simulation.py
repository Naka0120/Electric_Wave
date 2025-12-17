import unittest
from src.electric_wave_py.simulation import Simulation

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.simulation = Simulation()

    def test_initial_conditions(self):
        self.assertEqual(self.simulation.ey[0], 0)
        self.assertEqual(self.simulation.ey[-1], 0)

    def test_update_fields(self):
        initial_ey = self.simulation.ey.copy()
        self.simulation.update_fields()
        self.assertFalse((self.simulation.ey == initial_ey).all())

    def test_boundary_conditions(self):
        self.simulation.apply_boundary_conditions()
        self.assertEqual(self.simulation.ey[0], 0)
        self.assertEqual(self.simulation.ey[-1], 0)

if __name__ == '__main__':
    unittest.main()