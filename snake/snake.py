import pygame
import time
import random

# Init game
pygame.init()

l = 600
w = 600

screen = pygame.display.set_mode((l, w))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
gameplay=True
font = pygame.font.SysFont("arial", 25)
score = 0

# Init colours
black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255, 255, 255)

# Init snake position
x = 200
y = 200
dx = 0       
dy = 0
snake = 20

snake_blocks = []
snake_length = 1

# Snake draw function
def drawsnake(snake, body):
    for block in body:
        pygame.draw.rect(screen, green, [block[0], block[1], snake, snake])

# Food position
foodx = round(random.randrange(0, w - snake) / snake) * snake
foody = round(random.randrange(0, l - snake) / snake) * snake

# Game while loop
while gameplay:
    for event in pygame.event.get():
        # Events
        if event.type == pygame.QUIT:
            gameplay=False
        # Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -snake
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = snake
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -snake
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = snake
    
    # Game update
    if x >= l or x < 0 or y >= w or y < 0:
        gameplay = False

    for position in snake_blocks[:-1]:
            if position == [x, y]:
                gameplay = False

    x += dx
    y += dy

    # Fill display and draw score
    screen.fill(black)
    screen.blit(font.render("Score: " + str(score), True, white), [0, 0])

    # Draw snake
    snake_blocks.append([x, y])
    if len(snake_blocks) > score+1:
            del snake_blocks[0]
    drawsnake(snake, snake_blocks)

    # Draw food
    pygame.draw.rect(screen, red, [foodx, foody, snake, snake])
    pygame.display.update()

    if x == foodx and y == foody:
            score += 1

            foodx = round(random.randrange(0, w - snake) / snake) * snake
            foody = round(random.randrange(0, l - snake) / snake) * snake

            pygame.draw.rect(screen, red, [foodx, foody, snake, snake])

    clock.tick(10)

pygame.quit()
quit()