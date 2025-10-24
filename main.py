import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #begin game
    pygame.init()
    #initializes screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #fps (frames per second)
    clock = pygame.time.Clock()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #containerize the groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    #instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 #delta time

    #game loop - runs screen
    while True:
        #allows user to exit game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        #window filled
        screen.fill("black")
        
        #add player to the screen
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
