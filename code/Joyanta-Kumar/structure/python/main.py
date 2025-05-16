from random import choice
import pygame
pygame.init()

# Const
refreshRate = 60
width, height = 800, 600
tileSize = 100
rows, cols = height // tileSize, width // tileSize
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors (catppuccin)
dark = pygame.Color(24, 25, 38)
light = pygame.Color(202, 211, 245)
gray = pygame.Color(91, 96, 120)
green = pygame.Color(166, 218, 149)
blue = pygame.Color(138, 173, 244)
yellow = pygame.Color(238, 212, 159)

# Status
run = True

# Classes
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * tileSize
        self.y = row * tileSize
        self.walls = [False, False, False, False]   # [top, left, bottom, right]
    def draw(self, color = light, width = 0):
        pygame.draw.rect(window, color, (self.x+2, self.y+2, tileSize-4, tileSize-4), 0)
        # Walls
        color = blue
        if self.walls[0]: # top
            pygame.draw.line(window, color, (self.x+2, self.y+2), (self.x+tileSize-2, self.y+2), 2)
        if self.walls[2]: # bottom
            pygame.draw.line(window, color, (self.x+2, self.y+tileSize-2), (self.x+tileSize-2, self.y+tileSize-2), 2)
        if self.walls[1]: # left
            pygame.draw.line(window, color, (self.x+2, self.y+2), (self.x+2, self.y+tileSize-2), 2)
        if self.walls[3]: # right
            pygame.draw.line(window, color, (self.x+tileSize-2, self.y+2), (self.x+tileSize-2, self.y+tileSize-2), 2)


# Data
cells = [Cell(row, col) for row in range(rows) for col in range(cols)]
currentCell = cells[0]
nextCell = currentCell

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    window.fill(gray)

    for cell in cells:
        cell.draw(dark)

    currentCell.draw(light)
    clock.tick(refreshRate)