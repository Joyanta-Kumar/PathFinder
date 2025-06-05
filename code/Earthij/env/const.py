from pygame.display import set_mode
from pygame.time import Clock

rows = 40
cols = 80

tileSize = 20

window = set_mode((cols*tileSize+2, rows*tileSize+2))
clock = Clock()
