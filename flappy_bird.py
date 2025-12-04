import pygame
import sys
from settings import *
from bird import Bird
from pipes import PipeManager

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_big = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 35)

bird = Bird()
pipes = PipeManager()

game_active = False
game_over = False
score = 0
passed = []

while True:
    # ----------- INPUT -----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active and not game_over:
                    # Start game
                    game_active = True
                    bird = Bird()
                    pipes = PipeManager()
                    score = 0
                    passed = []

                elif game_over:
                    # Restart
                    game_over = False
                    game_active = True
                    bird = Bird()
                    pipes = PipeManager()
                    score = 0
                    passed = []

                else:
                    # Jump
                    bird.jump()

    # ----------- UPDATE -----------
    if game_active:
        bird.update()
        pipes.update()

        # Collision
        for p in pipes.pipes:
            if bird.rect.colliderect(p):
                game_active = False
                game_over = True

        if bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
            game_active = False
            game_over = True

        # Score
        for p in pipes.pipes:
            if p.y > HEIGHT // 2 and p.x + PIPE_WIDTH < bird.rect.x and p not in passed:
                score += 1
                passed.append(p)

    # ----------- DRAW -----------
    screen.fill(COLOR_BG)
    bird.draw(screen)
    pipes.draw(screen)

    # Score display
    if game_active:
        text = font_big.render(str(score), True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 10, 20))

    # Home screen
    if not game_active and not game_over:
        title = font_big.render("FLAPPY BIRD", True, (0, 0, 0))
        msg = font_small.render("Press SPACE to Start", True, (0, 0, 0))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

    # Game over
    if game_over:
        over = font_big.render("GAME OVER", True, (0, 0, 0))
        msg = font_small.render("Press SPACE to Restart", True, (0, 0, 0))
        screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 3))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)