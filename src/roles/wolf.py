from src.roles.entity import Entity

class Wolf(Entity):
    def __init__(self, status: str, x: int, y: int):
        super().__init__(status, x, y)
        