from pygame.display import set_mode
from pygame.time import Clock

rows = 7
cols = 9

tileSize = 120

window = set_mode((cols*tileSize+2, rows*tileSize+2))
clock = Clock()
