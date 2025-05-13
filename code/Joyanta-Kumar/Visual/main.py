import pygame

width = 800
height = 600
fps = 60

deltaTime = 0

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visual")
clock = pygame.time.Clock()

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.circle(window, "black", (self.x, self.y), 10)

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self):
        pygame.draw.line(window, "black", (self.start.x, self.start.y), (self.end.x, self.end.y), 2)

class Graph:
    def __init__(self, nodes = [], edges = []):
        self.edges = edges
        self.nodes = nodes
    
    def draw(self):
        for edge in self.edges:
            edge.draw()
        for node in self.nodes:
            node.draw()
    
    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
    
    def addEdge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)

n1 = Node(100, 100)
n2 = Node(400, 200)
n3 = Node(500, 400)
e1 = Edge(n1, n2)
e2 = Edge(n2, n3)
e3 = Edge(n1, n3)

graph = Graph([n1, n2], [e1])

graph.addNode(n3)
graph.addEdge(e2)
graph.addEdge(e3)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    window.fill("white")
    graph.draw()
    deltaTime = clock.tick(fps)