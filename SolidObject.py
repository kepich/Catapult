from Entity import Entity
from pygame import draw

class Rectangle(Entity):
    def __init__(self):
        super()
        self.isGhost = True
        self.color = (0, 0, 150)

    def render(self, scene):
        draw.rect(scene, self.color,)

    def update(self):
        pass
