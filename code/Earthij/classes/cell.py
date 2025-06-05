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
    
    def equals(self, cell):
        return self.row == cell.row and self.col == cell.col

    def __str__(self):
        cellData = f"{self.row},{self.col}"
        cellData += f",{"1" if self.walls["top"] else "0"}"
        cellData += f",{"1" if self.walls["left"] else "0"}"
        cellData += f",{"1" if self.walls["bottom"] else "0"}"
        cellData += f",{"1" if self.walls["right"] else "0"}"
        cellData += f",{"1" if self.visited else "0"}"
        return cellData
    
    def draw(self, cellColor=clr.cell, wallColor=None, border=0, padding=0,):
        x = size * self.col
        y = size * self.row
        if cellColor:
            rect(window, cellColor, (x+padding, y+padding, size-padding-padding, size-padding-padding), border)
        if wallColor:
            if self.walls["top"]:
                line(window, wallColor, (x, y), (x+size, y), 2)
            if self.walls["left"]:
                line(window, wallColor, (x, y), (x, y+size), 2)
            if self.walls["bottom"]:
                line(window, wallColor, (x, y+size), (x+size, y+size), 2)
            if self.walls["right"]:
                line(window, wallColor, (x+size, y), (x+size, y+size), 2)
    
