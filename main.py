from src.roles.environment import Environment
from src.sim.simulation import simulation

# Init
environment = Environment(grid_size=50, sheep_population = 0, wolf_population = 0)

simulation(environment, steps=100)