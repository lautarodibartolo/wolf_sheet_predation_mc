import matplotlib.pyplot as plt

def generate_plot(steps, grass_population, dead_grass_population, sheep_population, wolf_population):
    # plot grass population, dead grass population, sheep population, and wolf population over steps
    plt.plot(steps, grass_population, label="Grass", color="green")
    plt.plot(steps, dead_grass_population, label="Dead Grass", color="brown")
    plt.plot(steps, sheep_population, label="Sheep", color="grey")
    plt.plot(steps, wolf_population, label="Wolf", color="black")
    plt.xlabel("Steps")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Population vs. Steps")
    plt.savefig("media/population_vs_steps.png")
