import pygame

class ScoreCard(pygame.sprite.Sprite):
    containers = None

    def __init__(self):
        if hasattr(self, "containers"):  # Add container initialization
            super().__init__(self.containers)
        else:
            super().__init__()
        self.__kills = 0
        pygame.font.init()
        self.__font = pygame.font.Font(None, 36)

    def add_kill(self):
        self.__kills += 1

    def draw(self, screen):
        score_surface = self.__font.render(f"Kills: {self.__kills}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))