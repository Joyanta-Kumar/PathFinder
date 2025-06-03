from pygame.draw import line
from env.const import window, tileSize as size
import env.colors as clr

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f"{self.start} <---> {self.end}"
    
    def draw(self, color=clr.default, width=2):
        line(window, color, (self.start.col*size+size/2-width/2, self.start.row*size+size/2-width/2), (self.end.col*size+size/2-width/2, self.end.row*size+size/2-width/2), width)

    def contains(self, node):
        return self.start.equals(node) or self.end.equals(node)

    def equals(self, that):
        return self.contains(that.start) and self.contains(that.end)