from pygame.draw import rect, line
from const import tileSize, window, rows, cols
from color import bg

def drawCell(cell, color, borderWidth=0, wallWidth=1):
  rect(window, color, (tileSize*cell.col, tileSize*cell.row, tileSize, tileSize), borderWidth)
  if cell.wall["left"]:
    line(window, bg, (cell.col*tileSize, cell.row*tileSize), (cell.col*tileSize, cell.row*tileSize+tileSize), wallWidth)
  if cell.wall["right"]:
    line(window, bg, (cell.col*tileSize+tileSize, cell.row*tileSize), (cell.col*tileSize+tileSize, cell.row*tileSize+tileSize), wallWidth)
  if cell.wall["top"]:
    line(window, bg, (cell.col*tileSize, cell.row*tileSize), (cell.col*tileSize+tileSize, cell.row*tileSize), wallWidth)
  if cell.wall["bottom"]:
    line(window, bg, (cell.col*tileSize, cell.row*tileSize+tileSize), (cell.col*tileSize+tileSize, cell.row*tileSize+tileSize), wallWidth)

def drawCells(cells, color):
  if len(cells) != 0:
    for cell in cells:
      drawCell(cell, color)
  
def getIndex(row, col):
  return cols*row+col

def getIndeces(cells):
  indeces = []
  if len(cells) != 0:
    for cell in cells:
      indeces.append(getIndex(cell.row, cell.col))
  return indeces;

def getCell(row, col, cells):
  return cells[getIndex(row, col)]

def cellIsToVisit(cells):
  for cell in cells:
      if not cell.visited:
        return True
  return False

def deleteWall(currentCell, nextCell):
  # Same row
  if currentCell.row == nextCell.row:
    # Right
    if currentCell.col < nextCell.col:
      currentCell.wall["right"] = False
      nextCell.wall["left"] = False
    # Left
    elif currentCell.col > nextCell.col:
      currentCell.wall["left"] = False
      nextCell.wall["right"] = False
  # Same column
  elif currentCell.col == nextCell.col:
    # Bottom
    if currentCell.row < nextCell.row:
      currentCell.wall["bottom"] = False
      nextCell.wall["top"] = False
    # Top
    elif currentCell.row > nextCell.row:
      currentCell.wall["top"] = False
      nextCell.wall["bottom"] = False

def getNeighbors(cell, cells, ignoreWall=True):
  neighbors = []
  if cell.col != 0:       # Left
    if ignoreWall or not cell.wall["left"]:
      neighbors.append(getCell(cell.row, cell.col-1, cells))
  if cell.col != cols-1:  # Right
    if ignoreWall or not cell.wall["right"]:
      neighbors.append(getCell(cell.row, cell.col+1, cells))
  if cell.row != 0:       # Top
    if ignoreWall or not cell.wall["top"]:
      neighbors.append(getCell(cell.row-1, cell.col, cells))
  if cell.row != rows-1:  # Bottom
    if ignoreWall or not cell.wall["bottom"]:
      neighbors.append(getCell(cell.row+1, cell.col, cells))
  return neighbors

def getPaths(cell, cells, ignoreWall=True):
  neighbors = getNeighbors(cell, cells, ignoreWall)
  paths = []
  if len(neighbors) != 0:
    for cell in neighbors:
      if not cell.visited:
        paths.append(cell)
  return paths

