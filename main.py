import pygame
import constants
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import logging

# Add this near the top of your file
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    print(clock)
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    
    
    our_player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    our_asteroid_field = AsteroidField() 
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for update in updateable:
            update.update(dt)

        for asteroid in asteroids:
            if our_player.collision_check(asteroid):
                print("Game over!")
                event.type = pygame.QUIT
            
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    
    
if __name__ == "__main__":
    main()