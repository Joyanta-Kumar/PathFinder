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
        if not cell.walls["left"] or ignoreWalls:
            left = self.getCell(cell.row, cell.col-1)
            if left and (not left.visited or ignoreVisited):
                neighbors.append(left)
        if not cell.walls["right"] or ignoreWalls:
            right = self.getCell(cell.row, cell.col+1)
            if right and (not right.visited or ignoreVisited):
                neighbors.append(right)
        if not cell.walls["top"] or ignoreWalls:
            top = self.getCell(cell.row-1, cell.col)
            if top and (not top.visited or ignoreVisited):
                neighbors.append(top)
        if not cell.walls["bottom"] or ignoreWalls:
            bottom = self.getCell(cell.row+1, cell.col)
            if bottom and (not bottom.visited or ignoreVisited):
                neighbors.append(bottom)
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
                    if not self.perfect and choice([True, False, False]):
                        randomCell = choice(neighbors)
                        self.removeWall(currentCell, randomCell)
            elif not queue.empty():
                nextCell = queue.get()
            else:
                return False
            self.removeWall(currentCell, nextCell)
        return True
    
    def getDirection(self, current, target):
        direction = {"top":False,"left":False,"bottom":False,"right":False}
        text = ""
        if target.row < current.row:
            direction["top"] = True
            text += "Top"
        elif current.row < target.row:
            direction["bottom"] = True
            text += "Bottom"
        if target.col < current.col:
            direction["left"] = True
            text += "Left"
        elif current.col < target.col:
            direction["right"] = True
            text += "Right"
        print("On Target" if text == "" else text)
        if not direction["top"] and not direction["left"] and not direction["bottom"] and not direction["right"]:
            return None
        return direction

    def chooseNeighbor(self, current, target):
        neighbors = self.getNeighbors(current, ignoreVisited=False)
        direction = self.getDirection(current, target)
        choosenOne = None
        if not direction:
            return choosenOne

        top = self.getCell(current.row-1, current.col)
        left = self.getCell(current.row, current.col-1)
        bottom = self.getCell(current.row+1, current.col)
        right = self.getCell(current.row, current.col+1)

        if top:
            if not fn.cellInList(top, neighbors):
                top = None
        if left:
            if not fn.cellInList(left, neighbors):
                left = None
        if right:
            if not fn.cellInList(right, neighbors):
                right = None
        if bottom:
            if not fn.cellInList(bottom, neighbors):
                bottom = None


        if direction["right"]:
            if right:
                choosenOne = right
            elif top and direction["top"]:
                choosenOne = top
            elif bottom and direction["bottom"]:
                choosenOne = bottom
        elif direction["left"]:
            if left:
                choosenOne = left
            if top and direction["top"]:
                choosenOne = top
            elif bottom and direction["bottom"]:
                choosenOne = bottom
        
        if not choosenOne:
            choosenOne = choice(neighbors)
        
        return choosenOne