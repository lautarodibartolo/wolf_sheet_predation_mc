import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def generate_plot(iteration, steps, grass_population, dead_grass_population, sheep_population, wolf_population):
    # plot grass population, dead grass population, sheep population, and wolf population over steps
    plt.plot(steps, grass_population, label="Grass", color="green")
    plt.plot(steps, dead_grass_population, label="Dead Grass", color="brown")
    plt.plot(steps, sheep_population, label="Sheep", color="grey")
    plt.plot(steps, wolf_population, label="Wolf", color="black")
    plt.xlabel("Steps")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Population vs. Steps")
    plt.savefig(f"media/population_vs_steps_{iteration}.png")
    plt.clf()

def generate_avg_plot(iterations, steps, grass_population, dead_grass_population, sheep_population, wolf_population):
    df = pd.DataFrame({
        "iteration": iterations,
        "step": steps,
        "grass_population": grass_population,
        "dead_grass_population": dead_grass_population,
        "sheep_population": sheep_population,
        "wolf_population": wolf_population
    })
    
    # Plot the average grass_population with 80% confidence interval
    plt.figure(figsize=(12, 6))
    # sns.lineplot(data=df, x="step", y="grass_population", errorbar=('ci', 95), color="green", label="Grass")
    # sns.lineplot(data=df, x="step", y="dead_grass_population", errorbar=('ci', 95), color="brown", label="Dead Grass")
    sns.lineplot(data=df, x="step", y="sheep_population", errorbar=('ci', 95), color="grey", label="Sheep")
    sns.lineplot(data=df, x="step", y="wolf_population", errorbar=('ci', 95), color="black", label="Wolf")
    plt.title("Average Population with 95% Confidence Interval over Steps")
    plt.xlabel("Steps")
    plt.ylabel("Population")
    plt.legend()
    plt.savefig(f"media/avg_population_vs_steps.png")
    plt.clf()