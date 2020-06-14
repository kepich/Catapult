import GameSettings as GS
import pygame


class DisplayClass:
    def __init__(self):
        self.FPS = GS.FPS
        self.WINDOW_SIZE = GS.WINDOW_SIZE
        self.surface = None

        self.scene = pygame.display.set_mode(self.WINDOW_SIZE)

    def render(self, entities, environment, background):
        self.surface = pygame.Surface(self.WINDOW_SIZE)

        self.renderBackground(background)
        self.renderEnvironment(environment)
        self.renderEntities(entities)

        self.scene.blit(self.surface, (0, 0))
        pygame.display.update()

    def renderBackground(self, background):
        for obj in background:
            obj.render(self.surface)

    def renderEnvironment(self, environment):
        for obj in environment:
            obj.render(self.surface)

    def renderEntities(self, entities):
        for obj in entities:
            obj.render(self.surface)