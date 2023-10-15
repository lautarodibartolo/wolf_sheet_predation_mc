from src.roles.entities import DeadGrass, Sheep, Wolf
from src.utils.delete_images import delete_images
from src.utils.generate_gif import generate_gif
from src.utils.generate_plot import generate_plot

def simulation(environment, steps):
    if steps[-1] > 999999:
        raise ValueError("Steps must be less than 999999")
    
    delete_images()

    grass_population = []
    dead_grass_population = []
    sheep_population = []
    wolf_population = []
    for step in steps:
        if step % ((steps[-1] - 1) // 50) == 0:
            print(f"Progress: {round(step / steps[-1],2) * 100}%")
            environment.plot_environment(step)
        for i in range(environment.grid_size):
            for j in range(environment.grid_size):
                entity = environment.grid[i][j]
                if isinstance(entity, DeadGrass):
                    entity.grow()
                elif isinstance(entity, Sheep):
                    entity.update()
                elif isinstance(entity, Wolf):
                    entity.update()
        environment.plot_environment(step)
        grass_population.append(environment.grass_population)
        dead_grass_population.append(environment.dead_grass_population)
        sheep_population.append(environment.sheep_population)
        wolf_population.append(environment.wolf_population)
    
    generate_gif()
    generate_plot(steps, grass_population, dead_grass_population, sheep_population, wolf_population)
    