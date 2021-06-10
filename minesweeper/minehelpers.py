import pygame
import random
import math

cellsize = 10
black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255, 255, 255)

firstclick = True

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ismine = False
        self.flagged = False
        self.adj = 0
        self.blank = False
    
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
            try:
                if board[str(x) + str(y+cell)].ismine:
                    adjacent += 1
            except:
                pass
        # look one column left
        x -= 2
        for cell in range(3):
            cell -= 1
            try:
                if board[str(x) + str(y+cell)].ismine:
                    adjacent += 1
            except:
                pass
        # look one up
        x = int(xloc)
        y += 1
        try:
            if board[str(x) + str(y)].ismine:
                    adjacent += 1
        except:
            pass
        # look one down
        y -= 2
        try:
            if board[str(x) + str(y)].ismine:
                    adjacent += 1
        except:
            pass
        # store value
        self.adj = adjacent
        return adjacent

def gamestart(l, screen, colour, h):
    # Populate will cells
    # Using the size of grid, populate
    board = {}

    global cellsize
    cellsize = round((h/l))

    spacing = h/l
    for row in range(l):
        for cell in range(l):
            key = str(row) + str(cell)
            board[key] = Cell(row, cell)
            pygame.draw.rect(screen, colour, [(row)*spacing, (cell)*spacing, cellsize, cellsize], width=1)

    pygame.display.update()
    return board

def populatemines(l, board, num_mines, spacing, screen):
    if num_mines < l:
        x = str(random.randint(0, l-1))
        y = str(random.randint(0, l-1))
        if board[x+y].blank == False:
            board[x+y].ismine = True
            num_mines += 1
        else:
            populatemines(l, board, num_mines, spacing, screen)
        populatemines(l, board, num_mines, spacing, screen)
    else:
        return

def checkmine(l, screen, board, h, font):
    spacing = h/l
    x, y = pygame.mouse.get_pos()
    x = math.floor(x/spacing)*spacing
    y = math.floor(y/spacing)*spacing

    try:
        xloc = str(math.floor((x/spacing)))
        yloc = str(math.floor((y/spacing)))
        relmine = board[xloc + yloc]
    except:
        pass

    m1, m2, m3 = pygame.mouse.get_pressed(num_buttons=3)

    global firstclick

    # check if this is the first click
    if m1 and firstclick:
        # remove the mine "cover"
        pygame.draw.rect(screen, black, [x, y, cellsize, cellsize])
        relmine.blank = True
        #populate mines
        populatemines(l, board, 0, spacing, screen)
        firstclick = False
        # check surrounding mines and draw it on the screen
        adjcount(board, l)
        adj = relmine.adj
        screen.blit(font.render(str(adj), True, white), [x+(spacing/2)-10, y+(spacing/2)-10])
        popadj(xloc, yloc, board, screen, spacing, font, 0)
        return
    
    # mouse 1: delete a cell
    if m1 and not firstclick:
        # remove the mine "cover"
        pygame.draw.rect(screen, black, [x, y, cellsize, cellsize])
        # check if the player lost
        if relmine.ismine:
            pygame.quit()
            quit()
        # check surrounding mines and draw it on the screen
        adj = relmine.adj
        screen.blit(font.render(str(adj), True, white), [x+(spacing/2)-10, y+(spacing/2)-10])
    
    # mouse 2: flag a cell
    if m3 and not firstclick:
        relmine.flagged = True
        pygame.draw.rect(screen, blue, [x, y, cellsize, cellsize])

    pygame.display.update()

def adjcount(board, l):
    for row in range(l):
        for col in range(l):
            relmine = board[str(row) + str(col)]
            relmine.check(row, col, board)

def popadj(xloc, yloc, board, screen, spacing, font, depth):
    cellx = int(xloc)
    celly = int(yloc)

    if depth == 8:
        return

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 & y == 0:
                    continue
            try:
                newx = cellx+x
                newy = celly+y

                if board[str(newx) + str(newy)].adj == 0:
                    pygame.draw.rect(screen, black, [(newx)*spacing, (newy)*spacing, cellsize, cellsize])
                    popadj(newx, newy, board, screen, spacing, font, depth+1)
                else:
                    pygame.draw.rect(screen, black, [(newx)*spacing, (newy)*spacing, cellsize, cellsize])

                    adj = board[str(newx) + str(newy)].adj
                    screen.blit(font.render(str(adj), True, white), [((newx)*spacing)+(spacing/2)-10, ((newy)*spacing)+(spacing/2)-10])
            except:
                pass
