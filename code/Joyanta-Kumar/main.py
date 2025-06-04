from classes.maze import Maze
import pygame
from env.const import window, clock
import env.colors as clr
from random import choice
from classes.graph import Graph
from classes.node import Node
from classes.edge import Edge

maze = Maze()
graph = Graph()
# maze.generate()

start = maze.cells[0]
end = maze.getCell(maze.rows//2, maze.cols//2)

nextCell = start
currentCell = nextCell
neighbors = []
stack = []

perfectMaze = False
mazeGenerated = False
mazeScanned = False
foundEnd = False
graphTrimed = False


pygame.init()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    if not mazeGenerated:
        if maze.cellToVisit():
            currentCell = nextCell
            currentCell.visited = True
            neighbors = maze.getNeighbors(currentCell, ignoreVisited=False, ignoreWalls=True)
            if len(neighbors) != 0:
                stack.append(currentCell)
                nextCell = choice(neighbors)
                if not perfectMaze and choice([True, False]):
                    randomCell = choice(neighbors)
                    maze.removeWall(currentCell, randomCell)
            elif len(stack) != 0:
                nextCell = stack.pop()
            maze.removeWall(currentCell, nextCell)
        else:
            mazeGenerated = True
            currentCell = None
            nextCell = start
            stack = []
            for cell in maze.cells:
                cell.visited = False
    
    if mazeGenerated and not mazeScanned:
        if currentCell == end:
            foundEnd = True
        if not foundEnd:
            currentCell = nextCell
            currentCell.visited = True
            neighbors = maze.getNeighbors(currentCell, ignoreVisited=False, ignoreWalls=False)
            n1 = Node(currentCell.row, currentCell.col)
            graph.addNode(n1)
            nc = maze.getNeighbors(currentCell, ignoreVisited=True)
            for cell in nc:
                if cell.visited:
                    n2 = Node(cell.row, cell.col)
                    graph.addEdge(Edge(n1, n2))

            if len(neighbors) != 0:
                stack.append(currentCell)
                nextCell = choice(neighbors)
            elif len(stack) != 0:
                nextCell = stack.pop()
        
        elif foundEnd and not nextCell.visited:
            previousCell = currentCell
            currentCell = nextCell
            currentCell.visited = True
            neighbors = maze.getNeighbors(currentCell, ignoreVisited=True, ignoreWalls=False)
            nnc = []
            for cell in neighbors:
                if not cell.equals(previousCell):
                    nnc.append(cell)
            n1 = Node(currentCell.row, currentCell.col)
            graph.addNode(n1)
            nc = maze.getNeighbors(currentCell, ignoreVisited=True)
            for cell in nc:
                if cell.visited:
                    n2 = Node(cell.row, cell.col)
                    graph.addEdge(Edge(n1, n2))

            if len(nnc) != 0:
                stack.append(currentCell)
                nextCell = choice(nnc)
            elif len(stack) != 0:
                nextCell = stack.pop()
        else:
            nextCell = None
            currentCell = None
            stack = []
            neighbors = []
            mazeScanned = True
    if mazeScanned and not graphTrimed:
        for node in graph.nodes:
            n = graph.getNeighbors(node)
            if len(n) == 1 and not (node.equals(start) or node.equals(end)):
                graph.removeNode(node)
    

    pygame.display.flip()
    window.fill(clr.bg)
    
    maze.draw()
    for cell in stack:
        cell.draw(clr.stack, padding=35)
    for cell in neighbors:
        cell.draw(clr.neighbor, padding=35)
    if currentCell:
        currentCell.draw(clr.current)
    if nextCell:
        nextCell.draw(clr.neighbor, None, 0, 20)
    
    for edge in graph.edges:
        edge.draw(clr.edge)
    for node in graph.nodes:
        node.draw(clr.node)
    
    start.draw(clr.start, None, 3, 10)
    end.draw(clr.end, None, 3, 10)



    clock.tick(15 if mazeGenerated else 60)