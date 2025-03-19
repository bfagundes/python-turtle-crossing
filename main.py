from turtle import Screen
from player import Player
from score import Score
from game import Game
from config import(
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE
)

def setup_game_window():
    """Setups the game window"""
    screen = Screen()
    screen.title("Turtle Crossing!")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    # Establishes a grid-based coordinate system
    screen.setworldcoordinates(-GRID_SIZE, -GRID_SIZE, GRID_SIZE, GRID_SIZE)

    return screen

def setup_controls(screen, player):
    """Binds keyboard controls to the player object
    Args:
        screen (Screen):  The screen object from the Turtle library
        player (Player): The player object
    """
    screen.listen()
    screen.onkey(lambda: player.move_up(), "Up")
    screen.onkey(lambda: player.move_down(), "Down")
    screen.onkey(lambda: player.move_left(), "Left")
    screen.onkey(lambda: player.move_right(), "Right")

def level_up(screen, player, score, game):
    """Prepares the next level: Resets player position and increases the game speed.
    Args:
        screen (Screen): The screen object from the Turtle library
        player (Player): The player object
        score (Score): The score object
        game (Game): The game object
    """
    player.reset_position()
    game.level_up()
    game_loop(screen, player, score, game)

def game_loop(screen, player, score, game):
    """Handles the game loop and updates the screen
    Args:
        screen (Screen): The screen object from the Turtle library
        player (Player): The player object
        score (Score): The score object
        game (Game): The game object
    """
    game.update_obstacles()

    if player.reached_top():
        print(f"The player has reached the top!")
        score.update_score()
        screen.update()

        # Waits before starting the next level
        screen.ontimer(lambda: level_up(screen, player, score, game), 1000)
        return

    else:
        screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, player, score, game), 100)

def main():
    # Sets up the game window
    screen = setup_game_window()

    # Initializes the game objects
    player = Player()
    score = Score()
    game = Game()

    # Binds the keyboard controls
    setup_controls(screen, player)
    
    # Starts the game loop
    game_loop(screen, player, score, game)
    screen.mainloop()

if __name__ == "__main__":
    main()