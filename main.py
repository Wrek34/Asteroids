import pygame
from constants import *
from player import Player

def main():
    #begin game
    pygame.init()
    #initializes screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #fps (frames per second)
    clock = pygame.time.Clock()
    dt = 0 #delta time

    #instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop - runs screen
    while 0 == 0:
        #allows user to exit game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #window filled
        screen.fill("black", rect=None, special_flags=0)
        #add player to the screen
        player.draw(screen)
        pygame.display.flip()

        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
