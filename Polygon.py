from Entity import Entity
from pygame import draw


class Polygon(Entity):
    def __init__(self, vertices, color, isGhost):
        super().__init__()
        self.isGhost = isGhost
        self.color = color
        self.vertices = vertices

    def render(self, scene):
        draw.polygon(scene, self.color, self.vertices)

    def update(self):
        pass
