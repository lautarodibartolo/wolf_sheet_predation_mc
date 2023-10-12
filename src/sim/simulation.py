from src.roles.dead_grass import DeadGrass
from src.utils.delete_images import delete_images
from src.utils.generate_gif import generate_gif

def simulation(environment, steps):
    if steps > 999999:
        raise ValueError("Steps must be less than 999999")
    
    delete_images()

    for step in range(steps):
        for i in range(environment.grid_size):
            for j in range(environment.grid_size):
                if isinstance(environment.grid[i][j], DeadGrass):
                    environment.grid[i][j].grow()
        environment.plot_environment(step)
    
    generate_gif()
    
    
