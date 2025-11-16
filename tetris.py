import pygame, sys
from tetris_game import Game
from tetris_color import Color

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Color.white)
next_surface = title_font.render("Next", True, Color.white)
game_over_surface = title_font.render("GAME OVER", True, Color.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620)) #display setup
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
 
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_a and game.game_over == False: #left arrow key #K_A is A key 
                game.move_left()
            if event.key == pygame.K_d and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_s and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    #drawing
    score_value_surface = title_font.render(str(game.score), True, Color.white)

    screen.fill(Color.dark_blue) 
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Color. light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery))
    pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)