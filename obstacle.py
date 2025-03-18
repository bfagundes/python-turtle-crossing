from turtle import Turtle

class Obstacle(Turtle):
    
    def __init__(self, lane):
        """"Initializes the Obstacles object
        
        Args:
            lane (int): The number of the lane where the obstacle spawns"""
        super().__init__()
        
        
        self.lane = lane