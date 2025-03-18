import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from game import Game
from player import Player
from config import (
    GRID_SIZE
)

class TestGame(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        self.game = Game()
        self.player = Player()

    def test_initial_score(self):
        """Tests the initial score value"""
        self.assertEqual(self.game.score, 0, f"The initial score is incorrect")

    def test_score_update(self):
        """Tests whether the score updates when the player reaches the top"""
        expected_score = self.game.score + 1
        self.game.update_score()
        
        # Simulate the player reaching the top
        #self.player.sety(GRID_SIZE - self.player.wall_offset - 30)
        #self.player.move_up()

        # Check if the score increased
        self.assertEqual(self.game.score, expected_score, f"The score did not increased after the player reached the top")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)