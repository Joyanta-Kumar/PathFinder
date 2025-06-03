from env.const import window, tileSize as size
import env.colors as clr
from pygame.draw import rect, line

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = {
            "top": True,
            "left": True,
            "bottom": True,
            "right": True
        }

    def __str__(self):
        cellData = f"{self.row},{self.col}"
        cellData += f",{"1" if self.walls["top"] else "0"}"
        cellData += f",{"1" if self.walls["left"] else "0"}"
        cellData += f",{"1" if self.walls["bottom"] else "0"}"
        cellData += f",{"1" if self.walls["right"] else "0"}"
        return cellData
    
    def draw(self, cellColor=clr.default, wallColor=clr.wall, border=0, padding=0):
        x = size * self.col
        y = size * self.row
        rect(window, cellColor, (x+padding, y+padding, size-2*padding, size-2*padding), border)
        if self.walls["top"]:
            line(window, wallColor, (x, y), (x+size, y), 2) # top
        if self.walls["left"]:
            line(window, wallColor, (x, y), (x, y+size), 2) # left
        if self.walls["bottom"]:
            line(window, wallColor, (x, y+size), (x+size, y+size), 2) # bottom
        if self.walls["right"]:
            line(window, wallColor, (x+size, y), (x+size, y+size), 2) # right
    
