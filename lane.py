import random
from obstacle import Obstacle
from config import (
    GRID_SIZE,
    OBSTACLE_MIN_DISTANCE,
    OBSTACLE_COLORS,
    SLOW_OBSTACLE, FAST_OBSTACLE,
    SLOW_RATE, FAST_RATE,
    WILD_OBSTACLES
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
    
    def get_obstacle_color(self):
        """Returns the obstacle color
        Returns:
            string: The name of the color to be set on the obstacle. Can be used directly inside turtle.color(<color>)
        """
        rand_number = random.random()

        if not WILD_OBSTACLES:
            return random.choice(OBSTACLE_COLORS)
        
        else:

            if 0 < rand_number < SLOW_RATE:
                return SLOW_OBSTACLE
            
            elif SLOW_RATE+0.01 < rand_number < SLOW_RATE+FAST_RATE:
                return FAST_OBSTACLE
            
            else:
                return random.choice(OBSTACLE_COLORS)

    def spawn_obstacle(self):
        """Spawns a new obstacle into the lane"""
        color = self.get_obstacle_color()
        obstacle = Obstacle(self.number, self.ycor, color)
        self.obstacles.append(obstacle)

    def despawn_obstacles(self):
        """Despawns the obstacles that are past the left wall"""
        if not self.obstacles:
            return

        for obstacle in self.obstacles:

            # If the obstacle is past the left wall
            if obstacle.xcor() + obstacle.half_width < -GRID_SIZE:
                # Remove from the list
                self.obstacles.remove(obstacle)
                # Actually hide it and delete it from memory
                obstacle.hideturtle()
                obstacle.clear()
                del obstacle

    def move_obstacles(self):
        """Moves all the obstacles"""
        for obstacle in self.obstacles:
            obstacle.move()

    def increase_speed(self):
        """Increases the lane speed"""
        for obstacle in self.obstacles:
            obstacle.increase_speed()

    def detect_collision(self, player):
        """Detects a collision between the obstacles in the lane vs the player
        Args:
            player (Player): The player object
        Returns
            bool: True if a collision is detected, False otherwise
        """        
        for obstacle in self.obstacles:
            collision = abs(player.xcor() - obstacle.xcor()) < (player.size/2 + obstacle.half_width)

            if collision:
                return True

        return False