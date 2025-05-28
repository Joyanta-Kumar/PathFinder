from pygame.display import set_mode
from pygame.time import Clock

width = 1000
height = 1000
tileSize = 50
rows = height // tileSize
cols = width // tileSize

window = set_mode((width, height))
clock = Clock()
