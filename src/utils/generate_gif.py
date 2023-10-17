import os
import imageio
from src.utils.delete_images import delete_images

def generate_gif(iteration):
    images = []
    for filename in sorted(os.listdir("media")):
        if filename.startswith("simulation_"):
            pass
        elif filename.startswith("population_vs_steps"):
            pass
        else:
            images.append(imageio.imread("media/" + filename))
    delete_images()
    imageio.mimsave(f"media/simulation_{iteration}.gif", images)