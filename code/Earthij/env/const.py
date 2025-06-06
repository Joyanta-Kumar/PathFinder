from pygame.display import set_mode
from pygame.time import Clock

rows = 9
cols = 16

tileSize = 100

window = set_mode((cols*tileSize+2, rows*tileSize+2))
clock = Clock()
