import pygame

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ismine = 0
    
    def mine(self):
        self.ismine = 1

def gamestart(l, screen, colour, h):
    # Populate will cells
    # Using the size of grid, populate
    board = {}

    spacing = h/l
    for row in range(l):
        for cell in range(l):
            key = str(row) + str(cell)
            board[key] = Cell(row, cell)
            pygame.draw.rect(screen, colour, [(row+1)*spacing, (cell+1)*spacing, 10, 10])

def checkmine(x, y, board):
    pass