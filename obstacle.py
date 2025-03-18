from turtle import Turtle
from config import (
    GRID_SIZE, 
    OBSTACLE_STRETCH_WID
)

class Obstacle(Turtle):
    
    def __init__(self, lane, ycor, color):
        """"Initializes the Obstacles object
        
        Args:
            lane (int): The number of the lane where the obstacle spawns
            ycor (int): The Y coordinate for the obstacle
            color (string): The color for the obstacle
        """
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=OBSTACLE_STRETCH_WID, stretch_wid=1)
        self.half_width = (self.turtlesize()[1] * 20) / 2

        # Obstacle attributes
        self.lane = lane
        self.goto(GRID_SIZE, ycor)