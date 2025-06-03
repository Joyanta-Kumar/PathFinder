import pygame
from env.const import window, clock, rows, cols
import env.colors as clr
from classes.maze import Maze
from classes.graph import Graph
from classes.cell import Cell
from classes.node import Node
from classes.edge import Edge

maze = Maze()
# maze.generate()
# maze.dump()
maze.load()
graph = Graph()
graph.load(maze)
sGraph = Graph()

sGraph.nodes = graph.nodes.copy()
sGraph.edges = graph.edges.copy()

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
    start.draw(clr.stack, None, border=2, padding=10)
    end.draw(clr.end, None, border=2, padding=10)
    sGraph.draw()
    for node in sGraph.nodes:
        if len(sGraph.getNeighbors(node)) == 1 and not (node.equals(start) or node.equals(end)):
            node.draw("red", 10)
            sGraph.removeNode(node)
    clock.tick(30)

