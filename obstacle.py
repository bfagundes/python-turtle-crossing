from turtle import Turtle
from config import (
    GRID_SIZE, 
    OBSTACLE_STRETCH_WID,
    OBSTACLE_MOV_UNIT, OBSTACLE_MOV_INCREASE,
    FAST_OBSTACLE, SLOW_OBSTACLE,
    FAST_OBSTACLE_MODIFIER, SLOW_OBSTACLE_MODIFIER
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

        # Sets the obstacle speed
        self.mov_unit = OBSTACLE_MOV_UNIT
        if self.fillcolor() == SLOW_OBSTACLE:
            self.mov_unit = self.mov_unit * SLOW_OBSTACLE_MODIFIER
        
        elif self.fillcolor() == FAST_OBSTACLE:
            self.mov_unit = self.mov_unit * FAST_OBSTACLE_MODIFIER

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