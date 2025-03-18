from config import (
    ROW_HEIGHT, SCREEN_HEIGHT, GRID_SIZE
)

class Game():

    def __init__(self):
        """Initializes a lanes object"""

        # The num_lanes is equal to the screen height divided by the row height
        # minus two for the safe rows at the top and bottom
        self.num_lanes = int(SCREEN_HEIGHT / ROW_HEIGHT) -2

        # The start_y is from the bottom of the screen
        # + row height for the safe row at the bottom
        # +15 for the turtle offset
        self.start_y = -GRID_SIZE + ROW_HEIGHT + 15

        self.lanes = {}
        self.init_lanes()

    def init_lanes(self):

        for i in range(self.num_lanes):
            self.lanes[i+1] = self.start_y
            self.start_y += ROW_HEIGHT