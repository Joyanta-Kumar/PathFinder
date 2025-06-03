import env.colors as clr
from classes.node import Node
from classes.edge import Edge
from random import choice
from env.const import rows, cols

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.rows = rows
        self.cols = cols
    
    def __str__(self):
        return f"NODES: {len(self.nodes)}\nEDGES: {len(self.edges)}"

    def findNode(self, node):
        for index in range(len(self.nodes)):
            if node.equals(self.nodes[index]):
                return index
        return None
    
    def findEdge(self, edge):
        for index in range(len(self.edges)):
            if edge.equals(self.edges[index]):
                return index
        return None
    
    def addNode(self, node):
        if self.findNode(node) == None:
            self.nodes.append(node)
    
    def removeNode(self, node):
        index = self.findNode(node)
        if index == None:
            return
        left = self.nodes[:index]
        right = self.nodes[index+1:]
        self.nodes = left+right
        neighbors = self.getNeighbors(node)
        if len(neighbors) != 0:
            for neighbor in neighbors:
                self.removeEdge(Edge(node, neighbor))

    def getNeighbors(self, node):
        neighbors = []
        if node.row != 0:
            neighbor = Node(node.row-1, node.col)
            if self.findEdge(Edge(node, neighbor)) != None:
                neighbors.append(neighbor)
        if node.row != self.rows-1:
            neighbor = Node(node.row+1, node.col)
            if self.findEdge(Edge(node, neighbor)) != None:
                neighbors.append(neighbor)
        if node.col != 0:
            neighbor = Node(node.row, node.col-1)
            if self.findEdge(Edge(node, neighbor)) != None:
                neighbors.append(neighbor)
        if node.col != self.cols-1:
            neighbor = Node(node.row, node.col+1)
            if self.findEdge(Edge(node, neighbor)) != None:
                neighbors.append(neighbor)
        return neighbors
    
    def addEdge(self, edge):
        if self.findEdge(edge) == None and edge.start != edge.end:
            self.edges.append(edge)

    
    def removeEdge(self, edge):
        index = self.findEdge(edge)
        if index == None:
            return
        left = self.edges[:index]
        right = self.edges[index+1:]
        self.edges = left+right
        
    
    def draw(self):
        for edge in self.edges:
            edge.draw(clr.edge)
        for node in self.nodes:
            node.draw(clr.node)
    
    def load(self, maze):
        nextCell = maze.cells[0]
        currentCell = nextCell
        stack = []
        
        while maze.cellToVisit():
            currentCell = nextCell
            currentCell.visited = True
            neighbors = maze.getNeighbors(currentCell)
            self.addNode(Node(currentCell.row, currentCell.col))
            if len(neighbors) != 0:
                for cell in neighbors:
                    start = Node(currentCell.row, currentCell.col)
                    end = Node(cell.row, cell.col)
                    self.addEdge(Edge(start, end))
                stack.append(currentCell)
                nextCell = choice(neighbors)
            elif len(stack) != 0:
                nextCell = stack.pop()
    