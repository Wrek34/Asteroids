import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    while 0 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()
