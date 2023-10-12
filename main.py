from src.roles.environment import Environment

# Init
environment = Environment(grid_size=100,
                          sheep_population = 1000, sheep_reproduction_probability = 0.04, sheep_movement_probability = 0.4, sheep_hunted_probability = 0.1,
                          wolf_population = 200,
                          init_dead_grass_probability = 0.3, grass_growth_probability = 0.1)

environment.plot_environment()                          