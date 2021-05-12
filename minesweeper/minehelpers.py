import pygame
import random

cellsize = 10
black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255, 255, 255)

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ismine = False
        self.flagged = False
        self.adj = 0
    
    def mine(self):
        self.ismine = 1

    def check(self, xloc, yloc, board):
        x = int(xloc)
        y = int(yloc)
        adjacent = 0
        # look one column right
        x += 1
        for cell in range(3):
            cell -= 1
            if board[str(x) + str(y+cell)].ismine:
                adjacent += 1
        # look one column left
        x -= 2
        for cell in range(3):
            cell -= 1
            if board[str(x) + str(y+cell)].ismine:
                adjacent += 1
        # look one up
        x = int(xloc)
        y += 1
        if board[str(x) + str(y)].ismine:
                adjacent += 1
        # look one down
        y -= 2
        if board[str(x) + str(y)].ismine:
                adjacent += 1
        # store value
        self.adj = adjacent
        return adjacent


def gamestart(l, screen, colour, h):
    # Populate will cells
    # Using the size of grid, populate
    board = {}

    global cellsize
    cellsize = round((h/l)/3)

    spacing = h/l
    for row in range(l):
        for cell in range(l):
            key = str(row) + str(cell)
            board[key] = Cell(row, cell)
            pygame.draw.rect(screen, colour, [(row)*spacing, (cell)*spacing, cellsize, cellsize])

    populatemines(l, board, 0, spacing, screen)

    pygame.display.update()
    return board

def populatemines(l, board, num_mines, spacing, screen):
    if num_mines < l:
        x = str(random.randint(0, l-1))
        y = str(random.randint(0, l-1))
        board[x+y].ismine = True
        pygame.draw.rect(screen, white, [int(x)*spacing, int(y)*spacing, cellsize, cellsize])
        num_mines += 1
        populatemines(l, board, num_mines, spacing, screen)
    else:
        return

def checkmine(l, screen, board, h, font):
    spacing = h/l
    x, y = pygame.mouse.get_pos()
    x = round(x/spacing)*spacing
    y = round(y/spacing)*spacing

    try:
        xloc = str(round((x/spacing)))
        yloc = str(round((y/spacing)))
        relmine = board[xloc + yloc]
    except:
        pass

    m1, m2, m3 = pygame.mouse.get_pressed(num_buttons=3)
    
    # mouse 1: delete a cell
    if m1:
        # remove the mine "cover"
        pygame.draw.rect(screen, black, [x, y, cellsize, cellsize])
        # check if the player lost
        if relmine.ismine:
            pygame.quit()
            quit()
        # check surrounding mines and draw it on the screen
        adj = relmine.check(xloc, yloc, board)
        screen.blit(font.render(str(adj), True, white), [x, y])
    
    # mouse 2: flag a cell
    if m3:
        relmine.flagged = True
        pygame.draw.rect(screen, blue, [x, y, cellsize, cellsize])

    pygame.display.update()