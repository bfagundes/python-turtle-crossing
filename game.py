import random
from lane import Lane
from config import (
    ROW_HEIGHT, SCREEN_HEIGHT, GRID_SIZE, OBSTACLE_SPAWN_RATE
)

class Game():

    def __init__(self):
        """Initializes a Game object"""
        # The num_lanes is equal to the screen height divided by the row height
        # minus two for the safe rows at the top and bottom
        self.num_lanes = int(SCREEN_HEIGHT / ROW_HEIGHT) -2

        # The start_y is from the bottom of the screen
        # + row height for the safe row at the bottom
        # +15 for the turtle offset
        self.lane_y = -GRID_SIZE + ROW_HEIGHT + 15

        self.lanes = []
        self.init_lanes()

    def init_lanes(self):
        """Initializes the list of lanes, which will contain the obstacles"""
        for i in range(self.num_lanes):
            lane = Lane(i+1, self.lane_y)
            self.lanes.append(lane)
            self.lane_y += ROW_HEIGHT

    def spawn_obstacle(self):
        """Spawns a new obstacle into a random lane"""

        # Checks whether we should spawn a new obstacle based on the Spawn Rate
        if random.random() > OBSTACLE_SPAWN_RATE:
            return

        selected_lane = -1
        while selected_lane < 0:
            random_lane = random.randint(0, len(self.lanes)-1)

            if self.lanes[random_lane].can_spawn_obstacle():
                self.lanes[random_lane].spawn_obstacle()
                selected_lane = random_lane
                return
            
    def despawn_obstacles(self):
        """Despawns a obstacle once it hits the left wall"""
        for lane in self.lanes:
            lane.despawn_obstacles()

    def move_obstacles(self):
        """Moves all obstacles"""
        for lane in self.lanes:
            lane.move_obstacles()
            
    def update_obstacles(self):
        """Updates all obstacles:
        - Spawn new ones, if applicable
        - Moves all obstacles
        - Despawn the ones that have reached the left wall
        """
        self.spawn_obstacle()
        self.move_obstacles()
        self.despawn_obstacles()
