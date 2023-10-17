import os

def delete_images(all=False):
    if all:
        for filename in os.listdir("media"):
            os.remove("media/" + filename)
    else:
        for filename in os.listdir("media"):
            if filename.startswith("simulation_"):
                pass
            elif filename.startswith("population_vs_steps"):
                pass
            else:
                os.remove("media/" + filename)