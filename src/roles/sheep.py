from src.roles.entity import Entity
from src.roles.grass import Grass
from src.roles.dead_grass import DeadGrass
from src.roles.wolf import Wolf
import random

class Sheep(Entity):
    def __init__(self, x: int, y: int, environment, 
                 age: int = 0, max_age: int = 50, 
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

    def grow(self):
        self.age += 1
        if self.age >= self.max_age:
            self.die()

    def die(self):
        self.environment.grid[self.x][self.y] = DeadGrass(self.x, self.y, self.environment, self.environment.growth_probability)
        self.environment.sheep_population -= 1
        self.environment.dead_grass_population += 1

    def move(self):
        if random.random() <= self.movement_rate:
            old_x, old_y = self.x, self.y
            
            dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])  # Choose a random direction
            new_x, new_y = self.x + dx, self.y + dy
            
            # Periodic Boundary Conditions
            new_x = (self.x + dx) % len(self.environment.grid)
            new_y = (self.y + dy) % len(self.environment.grid[0])

            
            target_cell = self.environment.grid[new_x][new_y]

            if isinstance(target_cell, Grass):
                self.eat() 
                self.x, self.y = new_x, new_y
                self.environment.grid[new_x][new_y] = self
                self.environment.grid[old_x][old_y] = DeadGrass(old_x, old_y, self.environment, self.environment.growth_probability)
            elif isinstance(target_cell, DeadGrass):
                self.x, self.y = new_x, new_y
                self.environment.grid[new_x][new_y] = self
                self.environment.grid[old_x][old_y] = DeadGrass(old_x, old_y, self.environment, self.environment.growth_probability)
            elif isinstance(target_cell, Wolf):
                if random.random() <= self.hunted_rate:
                    self.environment.grid[self.x][self.y] = DeadGrass(self.x, self.y, self.environment, self.environment.growth_probability)
                    target_cell.energy += target_cell.sheep_energy
                    self.environment.sheep_population -= 1
                    self.environment.wolf_population += 1

        self.energy -= 1
        if self.energy <= 0:
            self.die()

    def eat(self):
        self.energy += self.grass_energy
        self.energy = min(self.energy, self.max_energy)
        self.environment.dead_grass_population += 1
        self.environment.grass_population -= 1

    def reproduce(self):
        if self.age >= self.reproduction_age and random.random() <= self.reproduction_rate:
            dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])  # Choose a random direction
            new_x, new_y = self.x + dx, self.y + dy

            # Periodic Boundary Conditions
            new_x = (self.x + dx) % len(self.environment.grid)
            new_y = (self.y + dy) % len(self.environment.grid[0])

            target_cell = self.environment.grid[new_x][new_y]
            
            if not isinstance(target_cell, Sheep) and not isinstance(target_cell, Wolf):
                new_sheep = Sheep(new_x, new_y, self.environment)
                if isinstance(target_cell, Grass):
                    self.environment.grid[new_x][new_y] = new_sheep
                    self.environment.sheep_population += 1
                    self.environment.grass_population -= 1
                else:
                    self.environment.grid[new_x][new_y] = new_sheep
                    self.environment.sheep_population += 1
                    self.environment.dead_grass_population -= 1
