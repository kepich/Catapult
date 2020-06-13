from Entity import Entity
from pygame import draw

class Rectangle(Entity):
    def __init__(self, x, y, width, height, color, isGhost=True):
        super().__init__()
        self.x = x
        self.y = y
        self.isGhost = isGhost
        self.color = color
        self.width = width
        self.height = height

    def render(self, scene):
        draw.rect(scene, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        pass
