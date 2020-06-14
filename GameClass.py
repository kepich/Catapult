import pygame

import GameSettings as GS
from DisplayClass import DisplayClass
from LevelFactory import LevelFactory


class GameClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.CLOCK = pygame.time.Clock()
        self.WINDOW_SIZE = GS.WINDOW_SIZE
        self.isPlaying = True

        self.DISPLAY = DisplayClass()

        self.level = LevelFactory.getLevel()

        self.entities = self.level.entities
        self.background = self.level.background

        pygame.display.set_mode(self.WINDOW_SIZE)

    def gameLoop(self):
        while self.isPlaying:
            self.update()
            self.DISPLAY.render(self.entities, self.background)
            self.CLOCK.tick(self.FPS)

    def update(self):
        exitEvent = pygame.event.get(pygame.QUIT)
        if exitEvent:
            self.isPlaying = False
            return

        self.entities.update()
