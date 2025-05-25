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
        screen.fill(color="Black")




if __name__ == "__main__":
    main()
