from pygame import draw

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, window):
        draw.line(window, "black", (self.start.x, self.start.y), (self.end.x, self.end.y), 2)