from src.roles.environment import Environment
from src.roles.entities import DeadGrass, Sheep, Wolf
from src.utils.delete_images import delete_images
from src.utils.generate_gif import generate_gif
from src.utils.generate_plot import generate_plot, generate_avg_plot
import random

def simulation(steps, iterations):
    if steps[-1] > 999999:
        raise ValueError("Steps must be less than 999999")
    
    delete_images(all=True)

    grid_size = 75
    sheep_pop = random.randint(20, 400)
    wolf_pop = random.randint(5, 100)
    grass_growth_probability = 0.125

    iteration_all = []
    steps_all = []
    grass_population_all = []
    dead_grass_population_all = []
    sheep_population_all = []
    wolf_population_all = []

    for iteration in iterations:
        print("Iteration:", iteration)
        environment = Environment(grid_size=grid_size, sheep_population=sheep_pop, wolf_population=wolf_pop, grass_growth_probability=grass_growth_probability)
        grass_population = []
        dead_grass_population = []
        sheep_population = []
        wolf_population = []
        for step in steps:
            if step % ((steps[-1] - 1) // 10) == 0:
                print(f"\tProgress: {round(step / steps[-1],2) * 100}%")
                # environment.plot_environment(step)
            for i in range(environment.grid_size):
                for j in range(environment.grid_size):
                    entity = environment.grid[i][j]
                    if isinstance(entity, DeadGrass):
                        entity.grow()
                    elif isinstance(entity, Sheep):
                        entity.update()
                    elif isinstance(entity, Wolf):
                        entity.update()
            grass_population.append(environment.grass_population)
            dead_grass_population.append(environment.dead_grass_population)
            sheep_population.append(environment.sheep_population)
            wolf_population.append(environment.wolf_population)

            iteration_all.append(iteration)
            steps_all.append(step)
            grass_population_all.append(environment.grass_population)
            dead_grass_population_all.append(environment.dead_grass_population)
            sheep_population_all.append(environment.sheep_population)
            wolf_population_all.append(environment.wolf_population)

        # generate_gif(iteration)
        # generate_plot(iteration, steps, grass_population, dead_grass_population, sheep_population, wolf_population)
        print()
    
    generate_avg_plot(iteration_all, steps_all, grass_population_all, dead_grass_population_all, sheep_population_all, wolf_population_all)
        