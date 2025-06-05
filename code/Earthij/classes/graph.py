import env.colors as clr
from classes.node import Node
from classes.edge import Edge
from random import choice
from env.const import rows, cols

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
    
    def __str__(self):
        return f"Nodes = {len(self.nodes)}\nEdges = {len(self.edges)}"
    
    def draw(self):
        for edge in self.edges:
            edge.draw(clr.edge, width=2)
        for node in self.nodes:
            node.draw(clr.node, radius=5)

    def nodeToVisit(self):
        count = 0
        for node in self.nodes:
            if node.visited:
                count += 1
        return len(self.nodes) - count
    
    def allNodeVisited(self):
        return self.nodeToVisit() == 0
    
    def containsNode(self, node):
        for n in self.nodes:
            if n.equals(node):
                # Don't return "node", node is identical to n, not a reference.
                # It is not in the graph.
                return n
        return None
    def containsEdge(self, edge):
        for e in self.edges:
            if e.equals(edge):
                # Same as n and node
                return e
        return None
    
    def getNode(self, row, col):
        return self.containsNode(Node(row, col))
    
    def getNeighbors(self, node, ignoreVisited=False, ignoreEdges=False):
        neighbors = []
        left = self.getNode(node.row, node.col-1)
        if left and (self.containsEdge(Edge(node, left)) or ignoreEdges):
            if not left.visited or ignoreVisited:
                neighbors.append(left)
        right = self.getNode(node.row, node.col+1)
        if right and (self.containsEdge(Edge(node, right)) or ignoreEdges):
            if not right.visited or ignoreVisited:
                neighbors.append(right)
        top = self.getNode(node.row-1, node.col)
        if top and (self.containsEdge(Edge(node, top)) or ignoreEdges):
            if not top.visited or ignoreVisited:
                neighbors.append(top)
        bottom = self.getNode(node.row+1, node.col)
        if bottom and (self.containsEdge(Edge(node, bottom)) or ignoreEdges):
            if not bottom.visited or ignoreVisited:
                neighbors.append(bottom)
        return neighbors
    
    def addNode(self, node):
        if not self.containsNode(node):
            self.nodes.append(node)
    
    def addEdge(self, edge):
        if  not edge.start.equals(edge.end) and not self.containsEdge(edge):
            self.edges.append(edge)
