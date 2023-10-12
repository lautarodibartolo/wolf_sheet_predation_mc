# Wolf-Sheep Predation Model

The Wolf-Sheep Predation model is a simple ecological model that illustrates the predator-prey dynamics between wolves and sheep in a shared environment. This model provides insights into how the interaction between predator and prey species can impact their populations over time. The primary components of this model include wolves, sheep, and grass, each with distinct behaviors and characteristics:

## Components:

### Sheep:
- **Reproduction**: Sheep have a certain probability of reproducing at each time step.
- **Grazing**: Sheep eat grass to survive. If there's no grass, they might die due to starvation.
- **Movement**: Sheep move randomly within the environment.

### Wolves:
- **Reproduction**: Wolves have a certain probability of reproducing at each time step.
- **Hunting**: Wolves hunt sheep for survival. Their hunting success rate affects their energy level and reproduction capability.
- **Movement**: Wolves move randomly within the environment, though they might have a tendency to follow sheep.

### Grass:
- **Regrowth**: Grass regrows at a certain rate, providing food for the sheep.

## Dynamics:

The model runs over a series of time steps, and in each step, the following occurs:
1. Sheep move, graze, and possibly reproduce.
2. Wolves move, hunt, and possibly reproduce.
3. Old wolves and sheep may die.
4. Grass regrows.

The interactions between wolves, sheep, and grass lead to complex dynamics that can result in oscillations of the population sizes, extinction of one or both species, or equilibrium states under certain conditions.

## Monte Carlo Simulation:

In our implementation, we employ the Monte Carlo method to simulate the model over many iterations. This statistical simulation method allows us to model the probability of different outcomes in this complex system, taking into account the inherent randomness in the interactions between wolves, sheep, and grass. By running the simulation over many iterations, we can analyze the distribution of possible outcomes and understand how different parameters affect the ecosystem dynamics.

## Setup and Running:

Instructions for setting up and running the simulation will be provided in subsequent sections.
