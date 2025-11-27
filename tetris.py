import pygame, sys
from tetris_game import Game
from tetris_color import Color

#initalise the pygame moduals 
pygame.init()

#renders the ui and text areas 
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Color.white)
next_surface = title_font.render("Next", True, Color.white)
game_over_surface = title_font.render("GAME OVER", True, Color.white)

#creats the rectangles that the score and next block will be displayed 
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#display setup
screen = pygame.display.set_mode((500, 620)) 
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

#creates a new game 
game = Game()

#automatically moves the block down every 200ms 
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

#game loop 
while True:
    #if the played closes the window the program closes 
    for event in pygame.event.get():
        #restarts the game if the user makes an input 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #keyboard inputs for movment 
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_a and game.game_over == False: #A key move left 
                game.move_left()
            if event.key == pygame.K_d and game.game_over == False: #D key move right
                game.move_right()
            if event.key == pygame.K_s and game.game_over == False: #S key move down / earn points
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_SPACE and game.game_over == False: #SPACE key rotate block
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    #drawing the game board and extras 
    score_value_surface = title_font.render(str(game.score), True, Color.white)

    #sets background color and draws score/next block secrion 
    screen.fill(Color.dark_blue) 
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    #if the game ends this shows a game over message 
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    #draws the block preview (next block) current block on screen and the grid
    pygame.draw.rect(screen, Color. light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery))
    pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
    game.draw(screen)

    #update the window and set fps limit to 60fps 
    pygame.display.update()
    clock.tick(60)