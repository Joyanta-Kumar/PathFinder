from pygame import draw

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, window):
        draw.circle(window, "black", (self.x, self.y), 10)