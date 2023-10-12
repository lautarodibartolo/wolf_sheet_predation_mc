import random

class Grass:
    """
    Represents a patch of grass in the simulation.
    """
    def __init__(self, status: str, x: int, y: int, growth_probability: float):
        """
        Initializes the grass patch with a given growth probability.
        """
        self.status = status
        self.x = x
        self.y = y
        self.growth_probability = growth_probability

    def grow(self):
        """
        Grows the grass based on the growth probability if it is currently dead.
        """
        if self.status == "Dead Grass" and random.random() < self.growth_probability:
            self.status = "Grass"
    
    def consume(self):
        """
        Represents the action of the grass being eaten by a sheep when a sheep moves to a grass position.
        """
        self.status = "Dead Grass"
