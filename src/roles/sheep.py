import random
from src.roles.grass import Grass
from src.roles.wolf import Wolf

class Sheep:
    """
    Represents a sheep in the simulation.
    """
    def __init__(self, x: int, y: int, reproduction_probability: float, movement_probability: float,hunted_probability: float, environment):
        """
        Initializes the sheep with a starting position, random energy level between 2 and 5, reproduction probability, and hunted probability.
        """
        self.status = "Sheep"
        self.x = x
        self.y = y
        self.energy = random.randint(2, 5)
        self.reproduction_probability = reproduction_probability
        self.movement_probability = movement_probability
        self.hunted_probability = hunted_probability
        self.environment = environment

    def move(self, grid):
        """
        Moves the sheep to one of the four possible directions.
        If the new position is Grass, the sheep consumes the grass. Otherwise, its energy decreases.
        """
        if random.random() < self.movement_probability:
            # Possible moves: right, left, up, down
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dx, dy = random.choice(moves)
            
            # Update the coordinates considering the grid boundaries (periodic boundary conditions)
            new_x = (self.x + dx) % len(grid)
            new_y = (self.y + dy) % len(grid[0])
            
            if isinstance(grid[new_x][new_y], Grass) and grid[new_x][new_y].status == "Grass":
                self.eat(grid[new_x][new_y])
                self.x = new_x
                self.y = new_y
            elif isinstance(grid[new_x][new_y], Grass) and grid[new_x][new_y].status != "Grass":
                self.energy -= 1
                self.x = new_x
                self.y = new_y
            elif isinstance(grid[new_x][new_y], Wolf):
                if random.random() < self.hunted_probability:
                    self.die(grid)
                else:
                    self.energy -= 1
        
        # If the sheep has no energy left, it dies
        if self.energy <= 0:
            self.die(grid)

    def eat(self, grass_patch):
        """
        Consumes a grass patch, increasing the sheep's energy.
        """
        grass_patch.consume()
        self.energy += 1
    
    def reproduce(self, grid):
        """
        Determines if the sheep reproduces based on the reproduction probability.
        If reproduction occurs, a new sheep is created in one of the neighboring positions, if possible.
        """
        if random.random() < self.reproduction_probability:
            # Possible moves: right, left, up, down
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(moves)
            
            for dx, dy in moves:
                new_x = (self.x + dx) % len(grid)
                new_y = (self.y + dy) % len(grid[0])
                
                # If the neighboring position contains Grass, the sheep can reproduce
                if isinstance(grid[new_x][new_y], Grass):
                    grid[new_x][new_y] = Sheep(new_x, new_y, self.reproduction_probability, self.hunted_probability, self.environment)
                    break  # Only one new sheep is created
    
    def die(self, grid):
        """
        Represents the death of the sheep, turning its position into Dead Grass.
        """
        grid[self.x][self.y] = Grass("Dead Grass", self.x, self.y, self.environment.growth_probability)