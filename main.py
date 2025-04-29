# imported files
import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #initializes pygame
    pygame.init()   

    #creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # X button in top right quits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        # ends game if player runs into an asteroid
        for obj in asteroids:
            if obj.check_collision(player) == True:
                print("Game Over!")
                sys.exit()
            for bullet in shot:
                if bullet.check_collision(obj) == True:
                    bullet.kill()
                    obj.kill()
                    obj.split()
        # draws objects on screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # limits fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")