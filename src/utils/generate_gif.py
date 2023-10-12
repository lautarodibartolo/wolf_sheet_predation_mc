import os
import imageio
from src.utils.delete_images import delete_images

def generate_gif():
    images = []
    for filename in sorted(os.listdir("media")):
        images.append(imageio.imread("media/" + filename))
    delete_images()
    imageio.mimsave("media/simulation.gif", images)