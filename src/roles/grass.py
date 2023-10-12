from src.roles.entity import Entity
class Grass(Entity):
    def __init__(self, status: str, x: int, y: int, growth_probability: float):
        super().__init__(status, x, y)
        self.growth_probability = growth_probability