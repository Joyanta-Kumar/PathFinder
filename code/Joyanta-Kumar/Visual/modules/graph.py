class Graph:
    def __init__(self, nodes = [], edges = []):
        self.edges = edges
        self.nodes = nodes
    
    def draw(self, window):
        for edge in self.edges:
            edge.draw(window)
        for node in self.nodes:
            node.draw(window)
    
    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
    
    def addEdge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)