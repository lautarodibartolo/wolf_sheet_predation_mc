import random
from src.roles.entity import Entity
from src.roles.grass import Grass

class DeadGrass(Entity):
    def __init__(self, x: int, y: int, environment, growth_probability: float):
        super().__init__(x, y, environment)
        self.color = (139, 69, 19) # Brown
        self.growth_probability = growth_probability
    
    def grow(self):
        if random.random() < self.growth_probability:
            self.environment.grid[self.x][self.y] = Grass(self.x, self.y, self.environment)
            self.environment.dead_grass_population -= 1
            self.environment.grass_population += 1