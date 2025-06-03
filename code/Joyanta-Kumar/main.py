import pygame
from env.const import window, clock, rows, cols
import env.colors as clr
from classes.maze import Maze
from classes.graph import Graph
from classes.cell import Cell
from classes.node import Node

maze = Maze()
maze.generate()
graph = Graph()
graph.load(maze)

start = Cell(0, 0)
end = Cell(rows//2, cols//2)

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
    maze.draw()
    graph.draw()
    clock.tick(60)

