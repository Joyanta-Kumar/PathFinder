import pygame

width, height = 800, 600
tileSize = 100
rows, cols = width // tileSize, height // tileSize
fps = 60
run = True

pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

stack = []

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def getRect(self):
        return (self.col * tileSize, self.row * tileSize, tileSize, tileSize)
    
    def draw(self, color = "orange", width = 1):
        pygame.draw.rect(window, color, self.getRect(), width)

cells = [Cell(row, col) for row in range(cols) for col in range(rows)]
currentCell = Cell(0, 0)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
                if event.key == pygame.K_UP:
                    currentCell.row -= 1
                elif event.key == pygame.K_DOWN:
                    currentCell.row += 1
                elif event.key == pygame.K_RIGHT:
                    currentCell.col += 1
                elif event.key == pygame.K_LEFT:
                    currentCell.col -= 1
    
    for cell in cells:
        cell.draw()
    currentCell.draw("white", 0)

    
    pygame.display.flip()
    window.fill("darkslategray")
    cell.draw()