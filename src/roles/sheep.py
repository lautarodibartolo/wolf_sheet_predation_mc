from src.roles.entity import Entity

class Sheep(Entity):
    def __init__(self, x: int, y: int, environment):
        super().__init__(x, y, environment)
        self.color = (255, 255, 255) # White
        