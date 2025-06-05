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
    
    
    for node in graph.nodes:
        n = graph.getNeighbors(node)
        if len(n) == 1 and not (node.equals(start) or node.equals(end)):
            graph.removeNode(node)


    pygame.display.flip()
    window.fill(clr.bg)
    maze.draw()
    start.draw(clr.start, border=3, padding=5)
    end.draw(clr.end, border=3, padding=5)
    graph.draw()
    clock.tick(30)