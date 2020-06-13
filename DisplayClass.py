import GameSettings as GS
import pygame

class DisplayClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.WINDOW_SIZE = GS.WINDOW_SIZE

        self.scene = pygame.display.set_mode(self.WINDOW_SIZE)

    def render(self, entities, enviroment):
        for obj in enviroment:
            obj.render(self.scene)
        pygame.display.update()