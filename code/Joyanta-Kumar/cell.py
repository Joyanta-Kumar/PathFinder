class Cell:
	def __init__(self,row,col):
		self.row=row
		self.col=col
		self.visited=False
		self.wall={"top": True,"left": True,"bottom": True,"right":True}
