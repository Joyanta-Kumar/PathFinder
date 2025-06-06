from env.const import rows, cols
import env.colors as clr
from classes.cell import Cell
from random import choice
from queue import Queue
import env.functions as fn

class Maze:
    def __init__(self, perfect=True):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell(row, col) for row in range(rows) for col in range(cols)]
        self.perfect = perfect
    
    def __str__(self):
        return f"{self.rows},{self.cols}" 
    
    def draw(self):
        for cell in self.cells:
            cell.draw(clr.cell if cell.visited else clr.bg, clr.wall)
    
    def cellToVisit(self):
        count = 0
        for cell in self.cells:
            if cell.visited:
                count += 1
        return len(self.cells) - count

    def allCellVisited(self):
        return self.cellToVisit() == 0

    def contains(self, cell):
        for c in self.cells:
            if c.equals(cell):
                # Don't return "cell", cell is identical to c, not a reference.
                # It is not in the maze.
                return c
        return None
    
    def getCell(self, row, col):
        return self.contains(Cell(row, col))
    
    def getNeighbors(self, cell, ignoreVisited=False, ignoreWalls=False):
        neighbors = []
        top = self.getCell(cell.row-1, cell.col)
        bottom = self.getCell(cell.row+1, cell.col)
        left = self.getCell(cell.row, cell.col-1)
        right = self.getCell(cell.row, cell.col+1)

        if top and (not top.visited or ignoreVisited):
            if ignoreWalls or (not cell.walls["top"]):
                neighbors.append(top)
        if left and (not left.visited or ignoreVisited):
            if ignoreWalls or (not cell.walls["left"]):
                neighbors.append(left)
        if bottom and (not bottom.visited or ignoreVisited):
            if ignoreWalls or (not cell.walls["bottom"]):
                neighbors.append(bottom)
        if right and (not right.visited or ignoreVisited):
            if ignoreWalls or (not cell.walls["right"]):
                neighbors.append(right)


        return neighbors

    def removeWall(self, cell, nextCell):
        if cell.row == nextCell.row:
            if cell.col < nextCell.col: # right
                cell.walls["right"] = False
                nextCell.walls["left"] = False
            elif cell.col > nextCell.col: # left
                cell.walls["left"] = False
                nextCell.walls["right"] = False
        elif cell.col == nextCell.col:
            if cell.row < nextCell.row: # bottom
                cell.walls["bottom"] = False
                nextCell.walls["top"] = False
            elif cell.row > nextCell.row: # bottom
                cell.walls["top"] = False
                nextCell.walls["bottom"] = False

    def reset(self, walls=True):
        for cell in self.cells:
            cell.visited = False
            if walls:
                cell.walls["top"] = True
                cell.walls["left"] = True
                cell.walls["bottom"] = True
                cell.walls["right"] = True

    
    def generate(self):
        self.reset()
        nextCell = choice(self.cells)
        currentCell = nextCell
        queue = Queue()
        while not self.allCellVisited():
            currentCell = nextCell
            currentCell.visited = True
            neighbors = self.getNeighbors(currentCell, ignoreWalls=True)
            if len(neighbors) != 0:
                if len(neighbors) == 1:
                    nextCell = neighbors[0]
                else:
                    queue.put(currentCell)
                    nextCell = choice(neighbors)
                    if not self.perfect and choice([True, False]):
                        randomCell = choice(neighbors)
                        self.removeWall(currentCell, randomCell)
            elif not queue.empty():
                nextCell = queue.get()
            else:
                return False
            self.removeWall(currentCell, nextCell)
        self.reset(walls=False)
        return True