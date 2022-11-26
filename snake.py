import pygame
import time
import random

pygame.init()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BLOCK_SIZE = 20 # Size of snake or food (also size of game grid square)
NUM_X_BLOCKS = 20 # Window width is a whole (integer) multiple of block size
NUM_Y_BLOCKS = 20 # same for window height
WINDOW_WIDTH = NUM_X_BLOCKS * BLOCK_SIZE
WINDOW_HEIGHT = NUM_Y_BLOCKS * BLOCK_SIZE

# Create window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set snake location to center of window (we divide number of window blocks by two)
snake_head_x = (NUM_X_BLOCKS // 2) * BLOCK_SIZE
snake_head_y = (NUM_Y_BLOCKS // 2) * BLOCK_SIZE
snake_direction = "up"
snake_body = [] # List of snake's body blocks' locations
snake_length = 1

# Create food in a random location inside game window
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
            # only allow movement to any direction if snake length is one (the game just started)
            # or if current direction is not opposite to target direction
            # for example:
            # if snake is long and current direction is up
            # the player cannot move down directly
            if event.key == pygame.K_UP and (snake_length == 1 or snake_direction != "down"):
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and (snake_length == 1 or snake_direction != "up"):
                snake_direction = "down"
            elif event.key == pygame.K_RIGHT and (snake_length == 1 or snake_direction != "left"):
                snake_direction = "right"
            elif event.key == pygame.K_LEFT and (snake_length == 1 or snake_direction != "right"):
                snake_direction = "left"
            elif event.key == pygame.K_ESCAPE:
                # Quit game if escape key is pressed
                is_game_running = False


    # Move snake based on direction
    if snake_direction == "up":
        snake_head_y -= BLOCK_SIZE
    elif snake_direction == "right":
        snake_head_x += BLOCK_SIZE
    elif snake_direction == "left":
        snake_head_x -= BLOCK_SIZE
    elif snake_direction == "down":
        snake_head_y += BLOCK_SIZE

    # Make snake appear from opposite side of window if it goes out of window's boundary
    if snake_head_x < 0:
        snake_head_x = WINDOW_WIDTH - BLOCK_SIZE
    elif snake_head_x >= WINDOW_WIDTH:
        snake_head_x = 0

    if snake_head_y < 0:
        snake_head_y = WINDOW_HEIGHT - BLOCK_SIZE
    elif snake_head_y >= WINDOW_HEIGHT:
        snake_head_y = 0
    
    # If snake head location is the same as food, then create new food
    # in a different location and grow snake
    if snake_head_x == food_x and snake_head_y == food_y:
        food_x = random.randint(0, NUM_X_BLOCKS - 1) * BLOCK_SIZE
        food_y = random.randint(0, NUM_Y_BLOCKS - 1) * BLOCK_SIZE
        snake_length += 1 # grow snake

    # Check if snake hits itself
    for snake_block_x, snake_block_y in snake_body:
        if snake_head_x == snake_block_x and snake_head_y == snake_block_y:
            # Game over, reset game
            snake_body.clear()
            snake_length = 1
            snake_head_x = (NUM_X_BLOCKS // 2) * BLOCK_SIZE
            snake_head_y = (NUM_Y_BLOCKS // 2) * BLOCK_SIZE
    
    # Store snake's head location in snake body list; so it can be drawn later;
    # drawing the last N snake head locations creates the illusion
    # of snake's movement
    snake_body.append((snake_head_x, snake_head_y))
    # If length of snake body is greater than snake length, delete oldest snake block
    # also part of the illusion
    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # Draw background
    window.fill(BLACK)

    # Draw food
    pygame.draw.rect(window, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for snake_block_x, snake_block_y in snake_body:
        pygame.draw.rect(window, YELLOW, (snake_block_x, snake_block_y, BLOCK_SIZE, BLOCK_SIZE))

    # Switch visible and invisible buffers
    pygame.display.flip()

    # Delay game so that snake is not so fast
    # we didn't need this on old computers ;)
    time.sleep(1/5)


pygame.quit()