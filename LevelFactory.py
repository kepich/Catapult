from abc import ABC, abstractmethod

from Level import Level


class LevelFactory(ABC):
    @abstractmethod
    def getLevel():
        return Level()
