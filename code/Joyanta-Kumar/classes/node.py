from pygame.draw import circle
from env.const import window, tileSize as size
import env.colors as clr

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
    
    def __str__(self):
        return f"{self.row},{self.col}"
    
    def draw(self, color=clr.node, radius=5):
        circle(window, color, (self.col*size+size/2, self.row*size+size/2), radius)
    
    def equals(self, that):
        return self.row == that.row and self.col == that.col