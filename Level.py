from Polygon import Polygon
from Rectangle import Rectangle
from GameSettings import WINDOW_SIZE

class Level:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.background = self.__backgroundInit()
        self.entities = self.__environmentInit()
        self.environment = list()

    def __backgroundInit(self):
        return [Rectangle(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1], (40, 120, 120))]

    def __environmentInit(self):
        environment = list()
        for floorObj in self.__createGround():
            environment.append(floorObj)
        return environment

    def __createGround(self):
        return [
            Rectangle(0, 300, 200, 200, (40, 120, 40), False),
            Polygon([[200, 300], [400, 450], [400, 600], [200, 600]], (40, 120, 40), False),
            Rectangle(400, 450, 400, 300, (40, 120, 40), False),
            ]
