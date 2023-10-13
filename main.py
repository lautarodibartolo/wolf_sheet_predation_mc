from src.roles.environment import Environment
from src.sim.simulation import simulation

# Init
environment = Environment(grid_size=50, sheep_population = 50, wolf_population = 0, grass_growth_probability = 0.1)

simulation(environment, steps=range(1000))