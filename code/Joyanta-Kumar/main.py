from classes.maze import Maze
import pygame
from env.const import window, clock, rows, cols
import env.colors as clr

maze = Maze()
maze.generate(perfect=False)

start = maze.cells[0]
end = maze.getCell(rows//2, cols//2)

graph = maze.scan(start, end)
pygame.init()
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        
    pygame.display.flip()
    window.fill(clr.bg)
    clock.tick(30)