import pygame 

from constants import * 


def main():
    pygame.init()

    print("Hell  from bootdev!")
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run=True
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill("black")
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
