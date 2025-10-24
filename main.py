import pygame
from constants import *

def main():
    #begin game
    pygame.init()
    #initializes screen
    screen = pygame.display.set_mode((1280, 720))

    #fps (frames per second)
    clock = pygame.time.Clock()
    dt = 0 #delta time

    #game loop - runs screen
    while 0 == 0:
        #allows user to exit game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #window filled
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()
        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
