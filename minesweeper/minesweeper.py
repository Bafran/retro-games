import pygame
import minehelpers as h # type: ignore

pygame.init()

l = 600
w = 600

cellgridsize = 12

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

board = h.gamestart(cellgridsize, screen, green, l)

while gameplay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay=False
    
    h.checkmine(cellgridsize, screen, board, l, font)

pygame.quit()
quit()