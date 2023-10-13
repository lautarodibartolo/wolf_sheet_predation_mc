import random

class Entity:
    def __init__(self, x: int, y: int, environment):
        self.x = x
        self.y = y
        self.environment = environment

class Grass(Entity):
    def __init__(self, x: int, y: int, environment):
        super().__init__(x, y, environment)
        self.color = (0, 128, 0) # Darker Green

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

class Sheep(Entity):
    def __init__(self, x: int, y: int, environment, 
                 age: int = 0, max_age: int = 50, 
                 energy: int = 10, grass_energy: int = 1, max_energy: int = 50,
                 reproduction_age: int = 5, reproduction_rate: float = 0.075,
                 movement_rate: float = 0.75):
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
        if isinstance(self.environment.grid[self.x][self.y], Sheep):
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

                self.energy -= 1
                if self.energy <= 0:
                    self.die()

    def eat(self):
        self.energy += self.grass_energy
        self.energy = min(self.energy, self.max_energy)
        self.environment.dead_grass_population += 1
        self.environment.grass_population -= 1

    def reproduce(self):
        if isinstance(self.environment.grid[self.x][self.y], Sheep):
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

class Wolf(Entity):
    def __init__(self, x: int, y: int, environment, 
                 age: int = 0, max_age: int = 100, 
                 energy: int = 20, sheep_energy: int = 5, max_energy: int = 50,
                 reproduction_age: int = 5, reproduction_rate: float = 0.065,
                 movement_rate: float = 0.85,
                 hunting_success_rate: float = 0.65):
        super().__init__(x, y, environment)
        self.color = (0, 0, 0) # Black

        self.age = age
        self.max_age = max_age
        self.energy = energy
        self.sheep_energy = sheep_energy
        self.max_energy = max_energy
        self.reproduction_age = reproduction_age
        self.reproduction_rate = reproduction_rate
        self.movement_rate = movement_rate
        self.hunting_success_rate = hunting_success_rate

    def update(self):
        self.grow()
        self.move()
        self.reproduce()

    def grow(self):
        self.age += 1
        if self.age >= self.max_age:
            self.die()

    def die(self):
        self.environment.grid[self.x][self.y] = Grass(self.x, self.y, self.environment)
        self.environment.wolf_population -= 1
        self.environment.grass_population += 1

    def move(self):
        if isinstance(self.environment.grid[self.x][self.y], Wolf):
            if random.random() <= self.movement_rate:
                old_x, old_y = self.x, self.y
                
                dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])  # Choose a random direction
                new_x, new_y = (self.x + dx) % len(self.environment.grid), (self.y + dy) % len(self.environment.grid[0])

                target_cell = self.environment.grid[new_x][new_y]

                if isinstance(target_cell, Sheep):
                    if random.random() <= self.hunting_success_rate:
                        self.eat()
                        self.x, self.y = new_x, new_y
                        self.environment.grid[new_x][new_y] = self
                        self.environment.sheep_population -= 1
                        self.environment.grid[old_x][old_y] = Grass(old_x, old_y, self.environment)
                        self.environment.grass_population += 1
                elif target_cell is None:
                    self.x, self.y = new_x, new_y
                    self.environment.grid[new_x][new_y] = self
                    self.environment.grid[old_x][old_y] = Grass(old_x, old_y, self.environment)

                self.energy -= 1
                if self.energy <= 0:
                    self.die()

    def eat(self):
        self.energy += self.sheep_energy
        self.energy = min(self.energy, self.max_energy)
        
    def reproduce(self):
        if isinstance(self.environment.grid[self.x][self.y], Wolf):
            if self.age >= self.reproduction_age and random.random() <= self.reproduction_rate:
                dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])  # Choose a random direction
                new_x, new_y = (self.x + dx) % len(self.environment.grid), (self.y + dy) % len(self.environment.grid[0])

                target_cell = self.environment.grid[new_x][new_y]
                
                if not isinstance(target_cell, Sheep) and not isinstance(target_cell, Wolf):
                    new_wolf = Wolf(new_x, new_y, self.environment)
                    if isinstance(target_cell, Grass):
                        self.environment.grid[new_x][new_y] = new_wolf
                        self.environment.wolf_population += 1
                        self.environment.grass_population -= 1
                    else:
                        self.environment.grid[new_x][new_y] = new_wolf
                        self.environment.wolf_population += 1
                        self.environment.dead_grass_population -= 1
