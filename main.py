import pygame

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Hell  from bootdev!")
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)
    pygame.quit()


if __name__ == "__main__":
    main()
