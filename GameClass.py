import pygame

import GameSettings as GS
from DisplayClass import DisplayClass
from Polygon import Polygon
from Rectangle import Rectangle


class GameClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.CLOCK = pygame.time.Clock()
        self.WINDOW_SIZE = GS.WINDOW_SIZE
        self.isPlaying = True

        self.DISPLAY = DisplayClass()

        self.entities = list()
        self.environment = list()

        self.environmentInitialising()
        pygame.display.set_mode(self.WINDOW_SIZE)

    def gameLoop(self):
        while self.isPlaying:
            self.update()
            self.DISPLAY.render(self.entities, self.environment)
            self.CLOCK.tick(self.FPS)

    def update(self):
        exitEvent = pygame.event.get(pygame.QUIT)
        if exitEvent:
            self.isPlaying = False
            return

        self.eventDispatcher(pygame.event.get())

    def eventDispatcher(self, events):
        for event in events:
            pass

    def environmentInitialising(self):
        self.environment.append(self.createSky())

        for floorObj in self.createGround():
            self.environment.append(floorObj)

    def createSky(self):
        return Rectangle(0, 0, self.WINDOW_SIZE[0], self.WINDOW_SIZE[1] , (40, 120, 120))

    def createGround(self):
        return [
            Rectangle(0, 300, 200, 200, (40, 120, 40), False),
            Polygon([[200, 300], [400, 450], [400, 600], [200, 600]], (40, 120, 40), False),
            Rectangle(400, 450, 400, 300, (40, 120, 40), False),
            ]
