from classes.edge import Edge
from classes.graph import Graph
from classes.node import Node
from env.const import rows, cols
import env.colors as clr
from classes.cell import Cell
from random import choice, randint
from queue import Queue

class Maze:
    def __init__(self):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell(row, col) for row in range(rows) for col in range(cols)]
    
    def __str__(self):
        return f"{self.rows},{self.cols}"
    
    def draw(self):
        for cell in self.cells:
            if cell.visited:
                cell.draw(clr.cell, clr.wall)
    
    def cellToVisit(self):
        count = 0
        for cell in self.cells:
            count += 1 if cell.visited else 0
        return self.rows*self.cols - count
    
    def getIndex(self, row, col):
        return self.cols*row+col
    
    def getCell(self, row, col):
        return self.cells[self.getIndex(row, col)]
    
    def getNeighbors(self, cell, ignoreVisited=False, ignoreWalls=False):
        neighbors = []
        if cell.row != 0:
            path = self.getCell(cell.row-1, cell.col)
            if (not path.visited or ignoreVisited) and (not cell.walls["top"] or ignoreWalls):
                neighbors.append(path)
        if cell.row != self.rows-1:
            path = self.getCell(cell.row+1, cell.col)
            if (not path.visited or ignoreVisited) and (not cell.walls["bottom"] or ignoreWalls):
                neighbors.append(path)
        if cell.col != 0:
            path = self.getCell(cell.row, cell.col-1)
            if (not path.visited or ignoreVisited) and (not cell.walls["left"] or ignoreWalls):
                neighbors.append(path)
        if cell.col != self.cols-1:
            path = self.getCell(cell.row, cell.col+1)
            if (not path.visited or ignoreVisited) and (not cell.walls["right"] or ignoreWalls):
                neighbors.append(path)
        return neighbors
    
    def removeWall(self, currentCell, nextCell):
        if currentCell.row == nextCell.row:
            if currentCell.col < nextCell.col: # right
                currentCell.walls["right"] = False
                nextCell.walls["left"] = False
            elif currentCell.col > nextCell.col: # left
                currentCell.walls["left"] = False
                nextCell.walls["right"] = False
        elif currentCell.col == nextCell.col:
            if currentCell.row < nextCell.row: # bottom
                currentCell.walls["bottom"] = False
                nextCell.walls["top"] = False
            elif currentCell.row > nextCell.row: # bottom
                currentCell.walls["top"] = False
                nextCell.walls["bottom"] = False
    
    def generate(self, perfect=True):
        self.cells = [Cell(row, col) for row in range(self.rows) for col in range(self.cols)]
        nextCell = choice(self.cells)
        currentCell = nextCell
        queue = Queue()

        while self.cellToVisit() != 0:
            currentCell = nextCell
            currentCell.visited = True
            neighbors = self.getNeighbors(currentCell, False, True)

            if len(neighbors) != 0:
                nextCell = choice(neighbors)
                if len(neighbors) > 1:
                    queue.put(currentCell)
                    if not perfect and choice([False, True]):
                        randomCell = choice(neighbors)
                        self.removeWall(currentCell, randomCell)
            elif not queue.empty():
                nextCell = queue.get()
            self.removeWall(currentCell, nextCell)

        for cell in self.cells:
            cell.visited = False
            # May be unnecessary
            if cell.row == 0:
                cell.walls["top"] = True
            elif cell.row == self.rows-1:
                cell.walls["bottom"] = True
            if cell.col == 0:
                cell.walls["left"] = True
            elif cell.col == self.cols-1:
                cell.walls["right"] = True
    
    def dump(self, fileName="zFile"):
        zFile = open(f"./zFiles/{fileName}.txt", "w")
        for cell in self.cells:
            zFile.write(str(cell)+"\n")
        zFile.close()
    
    def load(self, fileName="zFile"):
        self.cells = []
        zFile = open(f"./zFiles/{fileName}.txt", "r")
        for line in zFile:
            cellData = line.removesuffix("\n").split(",")
            for i in range(6):
                cellData[i] = int(cellData[i])
            cell = Cell(cellData[0], cellData[1])
            cell.walls["top"] = cellData[2] == 1
            cell.walls["left"] = cellData[3] == 1
            cell.walls["bottom"] = cellData[4] == 1
            cell.walls["right"] = cellData[5] == 1
            self.cells.append(cell)
        zFile.close()
    
    def solve(self, start, end):
        nextCell = start
        currentCell = nextCell
        stack = []
        while currentCell != end:
            currentCell = nextCell
            currentCell.visited = True
            neighbors = self.getNeighbors(currentCell, False, False)
            if len(neighbors) != 0:
                stack.append(currentCell)
                nextCell = choice(neighbors)
            elif len(stack) != 0:
                nextCell = stack.pop()
        for cell in self.cells:
            cell.visited = False
        return stack
    
    def scan(self, start, end):
        nextCell = start
        currentCell = nextCell
        stack = []
        graph = Graph()
        foundEnd = False

        while not foundEnd:
            if currentCell.equals(end):
                foundEnd = True
            currentCell = nextCell
            currentCell.visited = True
            neighbors = self.getNeighbors(currentCell)
            n1 = Node(currentCell.row, currentCell.col)
            graph.addNode(n1)
            nc = self.getNeighbors(currentCell, ignoreVisited=True)
            for cell in nc:
                if cell.visited:
                    n2 = Node(cell.row, cell.col)
                    graph.addEdge(Edge(n1, n2))

            if len(neighbors) != 0:
                stack.append(currentCell)
                nextCell = choice(neighbors)
            elif len(stack) != 0:
                nextCell = stack.pop()
        
        while foundEnd and not nextCell.visited:
            previousCell = currentCell
            currentCell = nextCell
            currentCell.visited = True
            neighbors = self.getNeighbors(currentCell, ignoreVisited=True, ignoreWalls=False)
            nnc = []
            for cell in neighbors:
                if not cell.equals(previousCell):
                    nnc.append(cell)
            n1 = Node(currentCell.row, currentCell.col)
            graph.addNode(n1)
            nc = self.getNeighbors(currentCell, ignoreVisited=True)
            for cell in nc:
                if cell.visited:
                    n2 = Node(cell.row, cell.col)
                    graph.addEdge(Edge(n1, n2))

            if len(nnc) != 0:
                stack.append(currentCell)
                nextCell = choice(nnc)
            elif len(stack) != 0:
                nextCell = stack.pop()
        return graph