from src.roles.environment import Environment
from src.sim.simulation import simulation

# Init
environment = Environment(grid_size=100, sheep_population = 0, wolf_population = 0, init_dead_grass_proportion = 0.5, grass_growth_probability = 0.01)

simulation(environment, steps=1000)