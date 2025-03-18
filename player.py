from turtle import Turtle
from config import (
    GRID_SIZE,
    ROW_HEIGHT
)

class Player(Turtle):
    
    def __init__(self):
        """"Initializes the Player object"""
        super().__init__()

        # Defines the player object characteristics
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.size = 20

        # Sets the initial position
        self.reset_position()

    def reset_position(self):
        """Resets the player position to the bottom of the screen."""
        self.goto(0, -GRID_SIZE + ROW_HEIGHT/2)