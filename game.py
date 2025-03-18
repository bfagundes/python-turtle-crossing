from turtle import Turtle
from config import (
    GRID_SIZE
)

class Game: 
    def __init__(self):
        """Initializes the game, with score tracking"""
        self.score = 0
        self.score_display = Turtle()
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.update_score_display()

    def update_score_display(self):
        """Updates the score display on the screen."""
        self.score_display.clear()
        self.score_display.goto(-255, 280)
        self.score_display.write(f"Level {self.score}", align="center", font=("Courier", 16, "bold"))

    def update_score(self):
        self.score += 1
        self.update_score_display()

    def display_game_over(self):
        """Displays the game-over message below the score."""
        self.score_display.goto(0, -100)
        self.score_display.write(f"Game Over!", align="center", font=("Courier", 24, "bold"))