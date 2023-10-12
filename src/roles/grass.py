import random
from src.roles.entity import Entity
class Grass(Entity):
    def __init__(self, x: int, y: int, environment):
        super().__init__(x, y, environment)
        self.color = (0, 128, 0) # Darker Green