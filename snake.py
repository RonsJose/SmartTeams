import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0) #Background
WHITE = (255, 255, 255) #Border
GREEN = (0, 255, 0) #Snake
RED = (255, 0, 0) #apple

# Game settings
CELL_SIZE = 20
FPS = 10

# Font
font = pygame.font.SysFont(None, 30)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(WINDOW, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(WINDOW, RED, (*food, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    WINDOW.blit(text, (5, 5))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    # Initial snake position and direction
    snake = [[100, 100]]
    dx, dy = CELL_SIZE, 0

    # Initial food position
    food = [random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)]

    score = 0
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_LEFT and dx == 0:
                        dx, dy = -CELL_SIZE, 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = CELL_SIZE, 0
                    elif event.key == pygame.K_UP and dy == 0:
                        dx, dy = 0, -CELL_SIZE
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dx, dy = 0, CELL_SIZE
                else:
                    if event.key == pygame.K_r:  # Restart
                        return True
                    elif event.key == pygame.K_q:  # Quit
                        return False

        if not game_over:
            # Move snake
            new_head = [snake[-1][0] + dx, snake[-1][1] + dy]
            snake.append(new_head)

            # Check collisions
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake[:-1]):
                game_over = True

            # Check if food eaten
            if new_head == food:
                score += 1
                food = [random.randrange(0, WIDTH, CELL_SIZE),
                        random.randrange(0, HEIGHT, CELL_SIZE)]
            else:
                snake.pop(0)

        # Draw everything
        WINDOW.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        draw_score(score)

        if game_over:
            # Display Game Over message prominently
            msg1 = font.render("GAME OVER", True, WHITE)
            msg2 = font.render("Press R to Restart or Q to Quit", True, WHITE)
            WINDOW.blit(msg1, (WIDTH // 4, HEIGHT // 3))
            WINDOW.blit(msg2, (WIDTH // 12, HEIGHT // 2))

        pygame.display.update()
        clock.tick(FPS)

    return False

def main():
    restart = True
    while restart:
        restart = game_loop()  # True if R pressed, False if Q

    pygame.quit()

if __name__ == "__main__":
    main()