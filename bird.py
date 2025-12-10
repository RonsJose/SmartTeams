import pygame
from settings import *

class Bird:
    def __init__(self):
        # Dummy image so main.py never crashes
        self.image = pygame.Surface((34, 24), pygame.SRCALPHA)
        self.image.fill((255, 255, 0))  # yellow fill

        self.rect = self.image.get_rect(center=(50, HEIGHT // 2))

        self.movement = 0
        self.gravity = 0.25

    def jump(self):
        self.movement = -6

    def update(self):
        self.movement += self.gravity
        self.rect.y += int(self.movement)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)