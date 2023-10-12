from src.roles.entity import Entity

class Wolf(Entity):
    def __init__(self, x: int, y: int, environment):
        super().__init__(x, y, environment)
        self.color = (0, 0, 0) # Black
        