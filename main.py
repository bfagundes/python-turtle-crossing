from turtle import Screen
from player import Player
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

def level_up(screen, player, game):
    player.reset_position()
    game_loop(screen, player, game)

def game_loop(screen, player, game):
    """Handles the game loop and updates the screen
    Args:
        screen (Screen): The screen object from the Turtle library
        player (Player): The player object
    """

    if player.reached_top():
        print(f"The player has reached the top!")
        game.update_score()
        # Increase obstacles speed
        screen.update()

        # Waits before starting the next level
        screen.ontimer(lambda: level_up(screen, player, game), 1000)
        return

    else:
        screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, player, game), 100)

def main():
    # Sets up the game window
    screen = setup_game_window()

    # Initializes the game objects
    player = Player()
    game = Game()

    # Binds the keyboard controls
    setup_controls(screen, player)
    
    # Starts the game loop
    game_loop(screen, player, game)
    screen.mainloop()

if __name__ == "__main__":
    main()