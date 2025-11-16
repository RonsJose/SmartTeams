import pygame, sys
from tetris_game import Game

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) #display setup
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
 
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #left arrow key #K_A is A key 
                game.move_left()
            if event.key == pygame.K_d:
                game.move_right()
            if event.key == pygame.K_s:
                game.move_down()
            if event.key == pygame.K_SPACE:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()
    
    screen.fill(dark_blue) #drawing
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)