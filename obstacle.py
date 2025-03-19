from turtle import Turtle
from config import (
    GRID_SIZE, 
    OBSTACLE_STRETCH_WID,
    OBSTACLE_MOV_UNIT, OBSTACLE_MOV_INCREASE
)

class Obstacle(Turtle):
    
    def __init__(self, lane, ycor, color):
        """"Initializes the Obstacles object
        
        Args:
            lane (int): The number of the lane where the obstacle spawns
            ycor (int): The Y coordinate for the obstacle
            color (string): The color for the obstacle
            type (string): the type of obstacle. "slow", "normal" or "fast"
        """
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=OBSTACLE_STRETCH_WID, stretch_wid=1)
        self.half_width = (self.turtlesize()[1] * 20) / 2

        # Sets the obstacle speed
        self.mov_unit = OBSTACLE_MOV_UNIT
        if self.fillcolor() == "green":
            self.mov_unit = self.mov_unit / 2
        
        elif self.fillcolor() == "red":
            self.mov_unit = self.mov_unit * 2

        # Obstacle attributes
        self.lane = lane
        self.goto(GRID_SIZE, ycor)

    def move(self):
        """Moves the obstacle"""
        self.setx(self.xcor() - self.mov_unit)

    def increase_speed(self):
        """Increases the obstacle speed"""
        self.mov_unit = self.mov_unit * (1 + OBSTACLE_MOV_INCREASE)

    def reset_speed(self):
        """Resets the obstacle speed to the starting speed"""
        self.mov_unit = OBSTACLE_MOV_UNIT