import pygame
import time

pygame.init()

window = pygame.display.set_mode((800, 800))

snake_x = 400
snake_y = 400
snake_direction = "up"
SNAKE_SIZE = 20

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
        snake_y -= SNAKE_SIZE
    elif snake_direction == "right":
        snake_x += SNAKE_SIZE
    elif snake_direction == "left":
        snake_x -= SNAKE_SIZE
    elif snake_direction == "down":
        snake_y += SNAKE_SIZE

    # Draw background
    window.fill((0, 0, 0))

    # Draw snake
    pygame.draw.rect(window, (255, 255, 0), (snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE))

    # Switch visible and invisible buffers
    pygame.display.flip()

    time.sleep(1/5)


pygame.quit()