import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from lane import Lane
from config import (
    GRID_SIZE,
    OBSTACLE_MOV_UNIT
)

class TestLane(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        self.lane = Lane(1, -255)

    def test_can_spawn_empty_lane(self):
        """Test whether the can_spawn method returns the expected value whe nthe lane is empty"""
        self.assertTrue(self.lane.can_spawn_obstacle(), f"Empty lane does not allow a new spawn")

    def test_can_spawn_ocupied_lane(self):
        """Test whether the can_spawn method returns the expected value when the lane has obstacles"""
        # Spawn an object on the lane
        self.lane.spawn_obstacle()
        with self.subTest("Lane has one obstacle at the initial position"):
            self.assertFalse(self.lane.can_spawn_obstacle(), f"The lane is allowing a new spawn when it shouldn't. [A]")

        # Moves the object forward, but not enough to allow a new spawn
        self.lane.obstacles[0].setx(GRID_SIZE - OBSTACLE_MOV_UNIT)
        with self.subTest("Lane has one obstacle in a position that shouldnt allow a new spawn"):
            self.assertFalse(self.lane.can_spawn_obstacle(), f"The lane is allowing a new spawn when it shouldn't. [B]")

        # Moves the obstacle enough for allowing a new spawn
        self.lane.obstacles[0].setx(0)
        with self.subTest("Lane has one obstacle in a position that SHOULD allow a new spawn"):
            self.assertTrue(self.lane.can_spawn_obstacle(), f"The lane is not allowing a new spawn when it should. [C]")

    def test_spawn_obstacle(self):
        """Test whether a new obstacle is spawned correclty"""
        self.lane.spawn_obstacle()
        self.assertEqual(len(self.lane.obstacles), 1, f"Failed to spawn an obstacle")

    def test_despawn_obstacle(self):
        """Thes the obstacle despawning"""
        self.lane.spawn_obstacle()
        self.lane.obstacles[0].setx(-GRID_SIZE - 100)
        self.lane.spawn_obstacle()
        self.lane.despawn_obstacles()
        self.assertEqual(len(self.lane.obstacles), 1, f"Failed to despawn an obstacle")

    def test_move_obstacle(self):
        """Test the lane obstacle movement"""
        expected_x = GRID_SIZE - OBSTACLE_MOV_UNIT
        self.lane.spawn_obstacle()
        self.lane.move_obstacles()
        self.assertEqual(self.lane.obstacles[0].xcor(), expected_x, f"Failed to move the lane obstacles")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)