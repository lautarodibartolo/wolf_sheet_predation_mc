import random
from matplotlib import pyplot as plt
from PIL import Image
from src.roles.grass import Grass
from src.roles.sheep import Sheep

class Environment:
    """
    Represents the simulation environment where wolves, sheep, and grass interact.
    """
    def __init__(self, grid_size: int,
                 sheep_population: int, sheep_reproduction_probability: float, sheep_movement_probability: float, sheep_hunted_probability: float,
                 wolf_population: int, 
                 init_dead_grass_probability: int, grass_growth_probability: float):
        """
        Initializes the environment with a specified grid side and initial counts for sheep and wolves.
        """
        self.grid_size = grid_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        
        self.sheep_population = sheep_population
        self.sheep_reproduction_probability = sheep_reproduction_probability
        self.sheep_movement_probability = sheep_movement_probability
        self.sheep_hunted_probability = sheep_hunted_probability
        
        
        self.wolf_population = wolf_population
        
        self.growth_probability = grass_growth_probability
        self.grass_patches = (1 - init_dead_grass_probability) * (grid_size * grid_size - (sheep_population + wolf_population))
        self.dead_grass_patches = init_dead_grass_probability * (grid_size * grid_size - (sheep_population + wolf_population))
        

        self._randomly_assign_positions()
    
    def _randomly_assign_positions(self):
        """
        Randomly assign positions on the grid for sheep, wolves, grass patches, and dead grass.
        """
        # Generate all possible positions
        positions = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size)]
        
        # Shuffle the positions randomly
        random.shuffle(positions)
        
        # Assign positions to sheep, wolves, grass patches, and dead grass
        for idx, position in enumerate(positions):
            i, j = position
            if idx < self.sheep_population:
                self.grid[i][j] = Sheep(i, j, self.sheep_reproduction_probability, self.sheep_movement_probability, 
                                        self.sheep_hunted_probability, self)
            elif idx < self.sheep_population + self.wolf_population:
                self.grid[i][j] = "Wolf"
            elif idx < self.sheep_population + self.wolf_population + self.grass_patches:
                self.grid[i][j] = Grass("Grass", i, j, self.growth_probability)
            else:
                self.grid[i][j] = Grass("Dead Grass", i, j, self.growth_probability)
    
    def plot_environment(self):
        """
        Plots the environment as a pixel map using PIL with a darker green color for grass and brown for dead grass.
        """
        # Map each entity to a color with a darker green and brown for dead grass
        color_map = {
            "Grass": (0, 128, 0),  # Darker Green
            "Sheep": (255, 255, 255),  # White
            "Wolf": (0, 0, 0),   # Black
            "Dead Grass": (139, 69, 19)  # Brown
        }
        
        # Convert the grid to an image array based on the color mapping
        img_array = [[color_map[cell.status if (isinstance(cell, Grass) or isinstance(cell, Sheep)) else cell] for cell in row] for row in self.grid]
        img = Image.new('RGB', (self.grid_size, self.grid_size))
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixels[j, i] = img_array[i][j]

        # Display the pixel map
        plt.imshow(img)
        plt.axis('off')
        plt.show()