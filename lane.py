import random
from obstacle import Obstacle
from config import (
    GRID_SIZE,
    OBSTACLE_MIN_DISTANCE,
    OBSTACLE_MOV_UNIT,
    OBSTACLE_COLORS,
)

class Lane():

    def __init__(self, number, ycor):
        """Initializes a lane object
        Args:
            number (int): The number of the lane
            ycor (int): The Y coordinate for the lane
        """
        self.number = number
        self.ycor = ycor
        
        self.obstacles = []
        self.last_obstacle_pos = GRID_SIZE

    def can_spawn_obstacle(self):
        """Checks whether the lane can spawn a new obstacle. 
        Returns:
            bool: True if the lane can spawn a new obstacle, False otherwise.
        """

        # Allows spawning if the list is empty
        if not self.obstacles:
            return True

        # Finds the rightmost obstacle 
        rightmost_obstacle = max(self.obstacles, key=lambda obs: obs.xcor())

        # Gets the distance between the obstacle and the right wall
        distance = abs(GRID_SIZE - (rightmost_obstacle.xcor() + rightmost_obstacle.half_width))

        return distance >= OBSTACLE_MIN_DISTANCE

    def spawn_obstacle(self):
        """Spawns a new obstacle into the lane"""
        color = random.choice(OBSTACLE_COLORS)
        obstacle = Obstacle(self.number, self.ycor, color)
        self.obstacles.append(obstacle)

    def despawn_obstacles(self):
        """Despawns the obstacles that are past the left wall"""

        if not self.obstacles:
            return
    
        try:
            # Finds the lefmost obstacle
            leftmost_obstacle = min(self.obstacles, key=lambda obs: obs.xcor())

            # Finds the rightmost xcor for this obstacle
            xcor = leftmost_obstacle.xcor() + leftmost_obstacle.half_width

            # Checks the distance from left wall
            if xcor < -GRID_SIZE:

                # Removes the obstacle
                self.obstacles.remove(leftmost_obstacle)
        
        except ValueError:
            # Happens if the obstacles list becomes empty between checkings 
            pass

    def move_obstacles(self):
        """Moves all the obstacles"""
        for obstacle in self.obstacles:
            obstacle.setx(obstacle.xcor() - OBSTACLE_MOV_UNIT)