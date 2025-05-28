import pygame
import color as clr
import function as fn
import const
import cell
from random import choice

pygame.init()

cells = [cell.Cell(row, col) for row in range(const.rows) for col in range(const.cols)]


def generateMaze(cells):
	stack = []
	nextCell = cells[0]
	currentCell = nextCell
	while fn.cellIsToVisit(cells):
		currentCell = nextCell
		currentCell.visited = True
		paths = fn.getPaths(currentCell, cells)
		if len(paths) != 0:
			stack.append(currentCell)
			nextCell = choice(paths)
		else:
			nextCell = stack.pop()
		fn.deleteWall(currentCell, nextCell)
	for cell in cells:
		cell.visited = False


generateMaze(cells)
start = cells[0]
end = cells[-1]
stack = []
nextCell = start
currentCell = nextCell

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False

	if currentCell != end:
		currentCell = nextCell
		currentCell.visited = True
		paths = fn.getPaths(currentCell, cells, ignoreWall=False)
		if len(paths) != 0:
			stack.append(currentCell)
			nextCell = choice(paths)
		else:
			nextCell = stack.pop()


	pygame.display.flip()
	const.window.fill(clr.bg)
	fn.drawCells(cells, clr.fg)
	fn.drawCells(stack, clr.lblue)
	fn.drawCell(start, clr.dgreen, 5)
	fn.drawCell(end, clr.red, 5)
	const.clock.tick(60)
