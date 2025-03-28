# Game Window settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = SCREEN_WIDTH // 2
ROW_HEIGHT = 30

# Player settings
PLAYER_MOV_UNIT = 30

# Obstacle settings
OBSTACLE_STRETCH_WID = 2.5
OBSTACLE_MIN_DISTANCE = 100
OBSTACLE_MIN_DISTANCE_DECREASE = 0.025

OBSTACLE_SPAWN_RATE = 0.5
OBSTACLE_SPAWN_INCREASE = 0.025
OBSTACLE_MAX_SPAWN_RATE = 0.7

OBSTACLE_MOV_UNIT = 10
OBSTACLE_MOV_INCREASE = 0.2

OBSTACLE_COLORS = ["blue", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan"]

# When this is set to true the game has obstacles moving at different speeds
WILD_OBSTACLES = True
FAST_OBSTACLE = "red"
FAST_OBSTACLE_MODIFIER = 2
SLOW_OBSTACLE = "green"
SLOW_OBSTACLE_MODIFIER = 0.5

# These combined should not exceed 1 (100%)
# 1 - slow - fast = the rate for normal speed obstacles
FAST_RATE = 0.1
SLOW_RATE = 0.1