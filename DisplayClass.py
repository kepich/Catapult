import GameSettings as GS
import pygame


class DisplayClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.WINDOW_SIZE = GS.WINDOW_SIZE
        self.surface = None

        self.scene = pygame.display.set_mode(self.WINDOW_SIZE)

    def render(self, entities, background):
        self.surface = pygame.Surface(self.WINDOW_SIZE)

        self.renderBackground(background)
        self.renderEntities(entities)

        self.scene.blit(self.surface, (0, 0))
        pygame.display.update()

    def renderBackground(self, background):
        background.draw(self.scene)

    def renderEntities(self, entities):
        entities.draw(self.scene)
