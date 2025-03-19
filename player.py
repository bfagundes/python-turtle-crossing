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
        self.current_lane = 0

        # Offset from the walls
        self.wall_offset = 15

        # x Coordinates from start and end of the obstacle
        self.boundary_xmin = -GRID_SIZE + ROW_HEIGHT / 2
        self.boundary_xmax = GRID_SIZE - ROW_HEIGHT / 2

        # Sets the initial position
        self.reset_position()

    def reset_position(self):
        """Resets the player position to the bottom of the screen."""
        self.goto(self.wall_offset, self.boundary_xmin)
        self.current_lane = 0

    def move_up(self):
        """Moves the Player UP"""
        if self.ycor() < self.boundary_xmax:
            self.sety(self.ycor() + PLAYER_MOV_UNIT)
            self.current_lane += 1

    def move_down(self):
        """Moves the Player DOWN"""
        if self.ycor() > self.boundary_xmin:
            self.sety(self.ycor() - PLAYER_MOV_UNIT)
            self.current_lane -= 1

    def move_right(self):
        """Moves the Player RIGHT"""
        if self.xcor() < GRID_SIZE - ROW_HEIGHT:
            self.setx(self.xcor() + PLAYER_MOV_UNIT)

    def move_left(self):
        """Moves the Player LEFT"""
        if self.xcor() > self.boundary_xmin:
            self.setx(self.xcor() - PLAYER_MOV_UNIT)

    def reached_top(self):
        """Returns whether the player has reached the top row
        Returns:
            bool: True if the player has reached the top row, False otherwise
        """
        return self.ycor() >= self.boundary_xmax
    
    def get_current_lane(self):
        """Returns the player current lane
        Returns:
            int: The player's current lane
        """
        return self.current_lane