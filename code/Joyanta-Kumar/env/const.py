from pygame.display import set_mode
from pygame.time import Clock

rows = 11
cols = 13

tileSize = 80

window = set_mode((cols*tileSize+2, rows*tileSize+2))
clock = Clock()
