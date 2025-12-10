import pygame
import random
from settings import *

class PipeManager:
    def __init__(self):
        self.pipes = []

    def create_pipe(self):
        height = random.randint(150, 450)
        bottom = pygame.Rect(WIDTH, height, PIPE_WIDTH, HEIGHT - height)
        top = pygame.Rect(WIDTH, height - PIPE_GAP - HEIGHT, PIPE_WIDTH, HEIGHT)
        return bottom, top

    def update(self):
        for pipe in self.pipes:
            pipe.x -= PIPE_SPEED

        # Add pipes
        if not self.pipes or self.pipes[-1].x < 200:
            self.pipes.extend(self.create_pipe())

        # Remove off-screen pipes
        self.pipes = [p for p in self.pipes if p.x > -PIPE_WIDTH]

    def draw(self, screen):
        for pipe in self.pipes:
            pygame.draw.rect(screen, COLOR_PIPE, pipe)