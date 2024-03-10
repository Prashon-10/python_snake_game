import pygame
import time
import random

pygame.init()

# Defining the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Setup the game window
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake food setting process
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # initialize the snake
    snake_list = []
    length_of_snake = 1

    # Initialize the snake position and movement
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    # initialize the food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_display.fill(black)
            message("You Lost! Press C-Play Again or Q- Quit", red)
            our_snake(snake_block, snake_list)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Checking for collisions with the borders
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Updating the display
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Maintain the length of the snake
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Checking collisions with the snake itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        # Set the snake speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
