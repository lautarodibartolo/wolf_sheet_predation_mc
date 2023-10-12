import random
from src.roles.grass import Grass
from src.roles.sheep import Sheep

class Wolf:
    """
    Represents a wolf in the simulation.
    """
    def __init__(self, x: int, y: int, reproduction_probability: float, hunted_probability: float, environment):
        """
        Initializes the wolf with a starting position, random energy level between 2 and 5, reproduction probability, and hunted probability.
        """
        self.x = x
        self.y = y
        self.energy = random.randint(2, 5)
        self.reproduction_probability = reproduction_probability
        self.hunted_probability = hunted_probability
        self.environment = environment

    def move(self, grid):
        """
        Moves the wolf to one of the four possible directions.
        If the new position is a Sheep, the wolf consumes the sheep. Otherwise, its energy decreases.
        """
        # Possible moves: right, left, up, down
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(moves)
        
        # Update the coordinates considering the grid boundaries (periodic boundary conditions)
        new_x = (self.x + dx) % len(grid)
        new_y = (self.y + dy) % len(grid[0])
        
        # Check the new position
        if isinstance(grid[new_x][new_y], Sheep):
            self.eat(grid[new_x][new_y])
            self.x = new_x
            self.y = new_y
        else:
            self.energy -= 1

    def eat(self, sheep, grid):
        """
        Consumes a sheep, increasing the wolf's energy.
        """
        sheep.die(grid)
        self.energy += 2
    
    def reproduce(self, grid):
        """
        Determines if the wolf reproduces based on the reproduction probability.
        If reproduction occurs, a new wolf is created in one of the neighboring positions, if possible.
        """
        if random.random() < self.reproduction_probability:
            # Possible moves: right, left, up, down
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(moves)
            
            for dx, dy in moves:
                new_x = (self.x + dx) % len(grid)
                new_y = (self.y + dy) % len(grid[0])
                
                # If the neighboring position contains Grass or Dead Grass, the wolf can reproduce
                if isinstance(grid[new_x][new_y], Grass):
                    grid[new_x][new_y] = Wolf(new_x, new_y, self.reproduction_probability, self.hunted_probability, self.environment)
                    break  # Only one new wolf is created
    
    def die(self, grid):
        """
        Represents the death of the wolf, turning its position into Dead Grass.
        """
        grid[self.x][self.y] = Grass("Dead Grass", self.x, self.y, self.environment.growth_probability)
