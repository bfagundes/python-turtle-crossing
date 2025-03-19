import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from game import Game
from config import (
    OBSTACLE_MAX_SPAWN_RATE, OBSTACLE_SPAWN_INCREASE, OBSTACLE_SPAWN_RATE
)

class TestGame(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        self.game = Game()

    def test_increase_spawn_rate(self):
        """Tests whether the obstacles spawn rate increases correctly"""
        rate = OBSTACLE_SPAWN_RATE * (1+OBSTACLE_SPAWN_INCREASE)
        self.game.increase_spawn_rate()
        self.assertEqual(self.game.spawn_rate, rate, f"Obstacle failed to increase speed correctly")

    def test_max_spawn_rate(self):
        """Tests that the spawn rate does not exceed the max limit"""
        self.game.spawn_rate = OBSTACLE_MAX_SPAWN_RATE * 0.99
        self.game.increase_spawn_rate()
        self.assertLess(self.game.spawn_rate, OBSTACLE_MAX_SPAWN_RATE, f"Spawn rate exceeded the max limit")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)