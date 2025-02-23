import pygame
import circle_shape

class Asteroid(circle_shape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
