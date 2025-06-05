from env.const import window
from env.const import clock
import env.colors as clr
from classes.maze import Maze
from classes.graph import Graph
from classes.node import Node
from classes.edge import Edge
import pygame
from queue import Queue
from random import choice

maze = Maze(perfect=False)
graph = Graph()
maze.generate()
maze.reset(walls=False)


start = maze.cells[0]
end = maze.getCell(maze.rows//2, maze.cols//2)
nextCell = start
currentCell = nextCell
neighbors = []
stack = []


pygame.init()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_f:
                maze.generate()
    direction = maze.getDirection(currentCell, end)
    if direction:
        currentCell = nextCell
        currentCell.visited = True
        neighbors = maze.getNeighbors(nextCell, ignoreWalls=False, ignoreVisited=False)
        if len(neighbors) != 0:
            stack.append(currentCell)
            nextCell = maze.chooseNeighbor(currentCell, end)
        elif len(stack) != 0:
            nextCell = stack.pop()

    pygame.display.flip()
    window.fill(clr.bg)
    maze.draw()
    if nextCell:
        nextCell.draw(clr.neighbor, padding=5)
    currentCell.draw(clr.current)


