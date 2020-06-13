from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.isGhost = True
        self.width = 0
        self.height = 0

    @abstractmethod
    def update(self):
        raise NotImplementedError()

    @abstractmethod
    def render(self, scene):
        raise NotImplementedError()