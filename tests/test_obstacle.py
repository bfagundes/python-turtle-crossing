import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from obstacle import Obstacle
from config import ( 
    GRID_SIZE, OBSTACLE_MOV_UNIT, OBSTACLE_MOV_INCREASE
)

class TestObstacle(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        self.obstacle = Obstacle(1, -255, "black")

    def test_initial_speed(self):
        expected_speed = OBSTACLE_MOV_UNIT
        self.assertEqual(self.obstacle.mov_unit, expected_speed, f"Obstacle initial speed is incorrect")

    def test_move(self):
        """Test the obstacle movement"""
        expected_x = GRID_SIZE - OBSTACLE_MOV_UNIT
        self.obstacle.move()
        self.assertEqual(self.obstacle.xcor(), expected_x, f"Obstacle failed to move correctly")

    def test_increase_speed(self):
        expected_speed = OBSTACLE_MOV_UNIT * (1+OBSTACLE_MOV_INCREASE)
        self.obstacle.increase_speed()
        self.assertEqual(self.obstacle.mov_unit, expected_speed, f"Obstacle failed to increase speed correctly")

    def test_reset_speed(self):
        expected_speed = OBSTACLE_MOV_UNIT
        self.obstacle.increase_speed()
        self.obstacle.increase_speed()
        self.obstacle.reset_speed()
        self.assertEqual(self.obstacle.mov_unit, expected_speed, f"Obstacle initial speed is incorrect")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)