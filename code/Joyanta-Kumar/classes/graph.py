import env.colors as clr
from classes.node import Node
from classes.edge import Edge
from random import choice

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
    
    def __str__(self):
        return f"NODES: {len(self.nodes)}\nEDGES: {len(self.edges)}"

    def containsNode(self, node):
        for n in self.nodes:
            if node.equals(n):
                return True
        return False
    
    def containsEdge(self, edge):
        for e in self.edges:
            if edge.equals(e):
                return True
        return False
    
    def addNode(self, node):
        if not self.containsNode(node):
            self.nodes.append(node)
    
    def addEdge(self, edge):
        if not self.containsEdge(edge) and edge.start != edge.end:
            self.edges.append(edge)
    
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