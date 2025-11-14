import pygame 
import sys
from tetris_grid import Grid

pygame.init()
dark_blue = (44, 44, 127)

#display setup
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)