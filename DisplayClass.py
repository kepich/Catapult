import GameSettings as GS
import pygame

class DisplayClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.WINDOW_SIZE = GS.WINDOW_SIZE

        pygame.display.set_mode(self.WINDOW_SIZE)

    def render(self, entities, enviroment):
        pygame.display.update()