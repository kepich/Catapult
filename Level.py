import pygame


class Level:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.background = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
