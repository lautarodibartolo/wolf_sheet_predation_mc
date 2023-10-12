import os

def delete_images():
    for filename in os.listdir("media"):
        os.remove("media/" + filename)