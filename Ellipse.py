from abc import ABC

from pygame import draw

from Entity import Entity


class Ellipse(Entity):
    def __init__(self, x, y, width, height, color, isGhost=True):
        super().__init__()
        self.x = x
        self.y = y
        self.isGhost = isGhost
        self.color = color
        self.width = width
        self.height = height

    def update(self):
        pass

    def render(self, scene):
        draw.ellipse(scene, self.color, (self.x, self.y, self.width, self.height))

    def getVertices(self):
        pass

