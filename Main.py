import pygame
from GameClass import GameClass

pygame.init()

if __name__ == '__main__':
    game = GameClass()
    game.gameLoop()
