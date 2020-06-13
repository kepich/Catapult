import pygame
import GameSettings as GS

pygame.init()

def init():
    return GS.FPS, pygame.time.Clock(), GS.WINDOW_SIZE

def update():
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            return False

    return True

def render():
    pass

def main():
    FPS, clock, WINDOW_SIZE = init()

    pygame.display.set_mode(WINDOW_SIZE)

    isPlaying = True
    while isPlaying:
        isPlaying = update()
        render()
        clock.tick(FPS)

if __name__ == '__main__':
    main()