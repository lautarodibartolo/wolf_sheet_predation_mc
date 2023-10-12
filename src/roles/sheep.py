import random
from src.roles.entity import Entity
from src.roles.grass import Grass
from src.roles.dead_grass import DeadGrass
from src.roles.wolf import Wolf

class Sheep(Entity):
    def __init__(self, x: int, y: int, environment, 
                 age: int = 0, max_age: int = 0, 
                 energy: int = 10, grass_energy: int = 1, max_energy: int = 50,
                 reproduction_age: int = 5, reproduction_rate: float = 0.1,
                 movement_rate: float = 0.75,
                 hunted_rate: float = 0.5):
        super().__init__(x, y, environment)
        self.color = (255, 255, 255) # White

        self.age = age
        self.max_age = max_age
        self.energy = energy
        self.grass_energy = grass_energy
        self.max_energy = max_energy
        self.reproduction_age = reproduction_age
        self.reproduction_rate = reproduction_rate
        self.movement_rate = movement_rate
        self.hunted_rate = hunted_rate

    def update(self):
        self.grow()
        self.move()
        self.reproduce()

    def move(self):
        if isinstance(self.environment.grid[self.x][self.y], Sheep):
            if random.random() <= self.movement_rate:
                # check if to the position I want to move is grass, if it's grass or deadgrass: move it to that position and then execute eat
                # if it's wolf don't move and execute hunted()
                # if it's sheep don't do anything.
                pass
            self.energy -= 1

            if self.energy <= 0:
                self.die()
    
    def eat(self):
        if isinstance(self.environment.grid[self.x][self.y], Grass):
            self.energy += self.grass_energy
            self.energy = min(self.energy, self.max_energy)
            self.environment.grid[self.x][self.y] = Sheep(self.x, self.y, self.environment)
            self.environment.dead_grass_population -= 1
            self.environment.grass_population += 1
    
    def hunted(self):
        if isinstance(self.environment.grid[self.x][self.y], Wolf) and random.random() <= self.hunted_rate:
            self.environment.grid[self.x][self.y] = DeadGrass(self.x, self.y, self.environment, self.environment.growth_probability)
            self.environment.sheep_population -= 1
            self.environment.wolf_population += 1
    
    def reproduce(self):
        if isinstance(self.environment.grid[self.x][self.y], Sheep):
            if self.age > 5 and random.random() <= self.reproduction_rate:
                pass
    
    def grow(self):
        self.age += 1
        if self.age >= self.max_age:
            self.die()

    def die(self):
        self.environment.grid[self.x][self.y] = DeadGrass(self.x, self.y, self.environment, self.environment.growth_probability)
        self.environment.sheep_population -= 1
        self.environment.dead_grass_population += 1
