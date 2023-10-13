from src.roles.environment import Environment
from src.sim.simulation import simulation

# Init
environment = Environment(grid_size=500, sheep_population = 25000, wolf_population = 5000, grass_growth_probability = 0.15)

simulation(environment, steps=range(10000))