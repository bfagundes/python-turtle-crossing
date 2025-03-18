from turtle import Turtle
from config import (
    GRID_SIZE, ROW_HEIGHT,
    PLAYER_MOV_UNIT
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

        # Offset from the walls
        self.wall_offset = 15

        # Sets the initial position
        self.reset_position()

    def reset_position(self):
        """Resets the player position to the bottom of the screen."""
        self.goto(self.wall_offset, -GRID_SIZE + ROW_HEIGHT/2)

    def move_up(self):
        """Moves the Player UP"""
        if self.ycor() < GRID_SIZE - ROW_HEIGHT/2:
            self.sety(self.ycor() + PLAYER_MOV_UNIT)

    def move_down(self):
        """Moves the Player DOWN"""
        if self.ycor() > -GRID_SIZE + ROW_HEIGHT/2:
            self.sety(self.ycor() - PLAYER_MOV_UNIT)

    def move_right(self):
        """Moves the Player RIGHT"""
        if self.xcor() < GRID_SIZE - ROW_HEIGHT:
            self.setx(self.xcor() + PLAYER_MOV_UNIT)

    def move_left(self):
        """Moves the Player LEFT"""
        if self.xcor() > -GRID_SIZE + ROW_HEIGHT/2:
            self.setx(self.xcor() - PLAYER_MOV_UNIT)