from classes.node import Node
from classes.edge import Edge
from classes.graph import Graph
from random import choice
import env.colors as clr
from env.const import window, clock, rows, cols
import pygame
from classes.maze import Maze
import env.functions as fn
from math import sqrt

graph = Graph()
maze = Maze(perfect=False)
maze.generate()
start = maze.cells[0]
end = maze.getCell(rows//2, cols//2)
graph.load(maze, start, end)

pygame.init()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_f:  
                maze.generate()
                graph.load(maze, start, end)


    pygame.display.flip()
    window.fill(clr.bg)
    for cell in maze.cells:
        if cell.visited:
            cell.draw(clr.cell, clr.wall)
    start.draw(clr.start, padding=10, border=2)
    end.draw(clr.end, padding=10, border=2)
    graph.draw()
    clock.tick(60)