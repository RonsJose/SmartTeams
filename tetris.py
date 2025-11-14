import pygame, sys
from tetris_grid import Grid
from tetris_blocks import *

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) #display setup
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid() #calls class

block = TBlock()

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(dark_blue) #drawing
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)