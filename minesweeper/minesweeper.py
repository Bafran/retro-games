import pygame
import minehelpers as h # type: ignore

pygame.init()

l = 600
w = 600

screen = pygame.display.set_mode((l, w))
clock = pygame.time.Clock()
pygame.display.set_caption('Minesweeper')
gameplay = True
font = pygame.font.SysFont("arial", 25)

black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255, 255, 255)

h.gamestart(10, screen, green, l)
pygame.display.update()

while gameplay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay=False

pygame.quit()
quit()