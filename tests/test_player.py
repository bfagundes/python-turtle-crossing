import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from player import Player
from config import (
    GRID_SIZE, ROW_HEIGHT,
    PLAYER_MOV_UNIT
)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        self.player = Player()

        # Moving the player to the middle of the screen to avoid hitting the screen borders
        self.player.goto(0,0)

    def test_move_up(self):
        """Test the Player movement up"""
        expected_y = self.player.ycor() + PLAYER_MOV_UNIT
        self.player.move_up()
        self.assertEqual(self.player.ycor(), expected_y, f"Player failed to move UP correctly.")

    def test_move_down(self):
        """Test the Player movement down"""
        expected_y = self.player.ycor() - PLAYER_MOV_UNIT
        self.player.move_down()
        self.assertEqual(self.player.ycor(), expected_y, f"Player failed to move DOWN correctly.")

    def test_move_left(self):
        """Test the Player movement left"""
        expected_x = self.player.xcor() - PLAYER_MOV_UNIT
        self.player.move_left()
        self.assertEqual(self.player.xcor(), expected_x, f"Player failed to move LEFT correctly.")

    def test_move_right(self):
        """Test the Player movement right"""
        expected_x = self.player.xcor() + PLAYER_MOV_UNIT
        self.player.move_right()
        self.assertEqual(self.player.xcor(), expected_x, f"Player failed to move RIGHT correctly.")

    def test_reset_position(self):
        """Test the Player position reset"""
        expected_position = (15, -GRID_SIZE + ROW_HEIGHT/2)
        self.player.goto(0,0)
        self.player.reset_position()
        self.assertEqual((self.player.xcor(), self.player.ycor()), expected_position, f"Player failed to reset to initial position correctly.")

    def test_boundaries_up(self):
        """Test player bounds vs the upper wall"""
        expected_y = 285
        self.player.sety(expected_y)
        self.player.move_up()
        self.assertEqual(self.player.ycor(), expected_y, f"Player went out of bounds on the upper wall")

    def test_boundaries_down(self):
        """Test player bounds vs the lower wall"""
        expected_y = -285
        self.player.sety(expected_y)
        self.player.move_down()
        self.assertEqual(self.player.ycor(), expected_y, f"Player went out of bounds on the lower wall")

    def test_boundaries_right(self):
        """Test player bounds vs the right wall"""
        expected_x = 285
        self.player.setx(expected_x)
        self.player.move_right()
        self.assertEqual(self.player.xcor(), expected_x, f"Player went out of bounds on the right wall")

    def test_boundaries_down(self):
        """Test player bounds vs the left wall"""
        expected_x = -285
        self.player.setx(expected_x)
        self.player.move_left()
        self.assertEqual(self.player.xcor(), expected_x, f"Player went out of bounds on the left wall")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)