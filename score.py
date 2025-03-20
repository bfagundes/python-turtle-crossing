from turtle import Turtle
from config import GRID_SIZE

class Score: 
    def __init__(self):
        """Initializes the game, with score tracking"""
        self.score = 0
        self.high_score = 0
        self.score_display = Turtle()
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.update_score_display()
        self.load_high_score()

    def update_score_display(self):
        """Updates the score display on the screen."""
        self.score_display.clear()
        #self.score_display.goto(-255, 280)
        self.score_display.goto(-GRID_SIZE*0.8, GRID_SIZE*0.9)
        self.score_display.write(f"Level {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 16, "bold"))

    def update_score(self):
        """Increases the game score by one."""
        self.score += 1
        self.update_score_display()

    def display_game_over(self):
        """Displays the game-over message below the score."""
        self.score_display.goto(0, 0)
        self.score_display.write(f"Game Over!", align="center", font=("Courier", 16, "bold"))

    def update_high_score(self):
        """Updates the high score"""
        if self.score > self.high_score:
            self.high_score = self.score

            try:
                with open(file="high_score.txt", mode="w") as file:
                    file.write(self.high_score)
            except IOError as e:
                print(f"Failed to save the high score: {e}")

    def load_high_score(self):
        """Loads the saved high score from the high_score.txt file."""
        try:
            with open(file="high_score.txt", mode="r") as file:
                content = file.read()
                if len(content) == 0:
                    self.high_score = 0
                else:
                    self.high_score = int(content)

        except (IOError, ValueError) as e:
            self.high_score = 0
            print(f"Failed to load the high score: {e}")