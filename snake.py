import pygame
import time
import random

pygame.init()

BLOCK_SIZE = 20
NUM_X_BLOCKS = 20
NUM_Y_BLOCKS = 20
WINDOW_WIDTH = NUM_X_BLOCKS * BLOCK_SIZE
WINDOW_HEIGHT = NUM_Y_BLOCKS * BLOCK_SIZE

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

snake_x = (NUM_X_BLOCKS // 2) * BLOCK_SIZE
snake_y = (NUM_Y_BLOCKS // 2) * BLOCK_SIZE
snake_direction = "up"
snake_history = []
snake_length = 1

food_x = random.randint(0, NUM_X_BLOCKS - 1) * BLOCK_SIZE
food_y = random.randint(0, NUM_Y_BLOCKS - 1) * BLOCK_SIZE

is_game_running = True

while is_game_running:
    # Get user input
    for event in pygame.event.get():
        # Quit game if exit button is pressed
        if event.type == pygame.QUIT:
            is_game_running = False
        elif event.type == pygame.KEYDOWN:
            # Change snake direction based on arrow keys
            if event.key == pygame.K_UP:
                snake_direction = "up"
            elif event.key == pygame.K_DOWN:
                snake_direction = "down"
            elif event.key == pygame.K_RIGHT:
                snake_direction = "right"
            elif event.key == pygame.K_LEFT:
                snake_direction = "left"
            elif event.key == pygame.K_ESCAPE:
                # Quit game if escape key is pressed
                is_game_running = False


    # Move snake
    if snake_direction == "up":
        snake_y -= BLOCK_SIZE
    elif snake_direction == "right":
        snake_x += BLOCK_SIZE
    elif snake_direction == "left":
        snake_x -= BLOCK_SIZE
    elif snake_direction == "down":
        snake_y += BLOCK_SIZE
    
    # Add new snake block
    snake_history.append((snake_x, snake_y))
    # If greater than snake length, delete oldest snake block
    if len(snake_history) > snake_length:
        snake_history.pop(0)

    # Draw background
    window.fill((0, 0, 0))

    # Draw food
    pygame.draw.rect(window, (255, 0, 0), (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for snake_x, snake_y in snake_history:
        pygame.draw.rect(window, (255, 255, 0), (snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE))

    # Switch visible and invisible buffers
    pygame.display.flip()

    time.sleep(1/5)


pygame.quit()