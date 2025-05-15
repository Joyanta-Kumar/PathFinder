from modules.node import Node
from modules.edge import Edge
from modules.graph import Graph

from random import randint, choice
import pygame
pygame.init()

fps = 60
deltaTime = 0
width, height = 800, 600
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

graph = Graph([], [])


def addRandomPoint():
    graph.addNode(Node(randint(0, width), randint(0, height)))

def addRandomEdge():
    start = choice(graph.nodes)
    end = choice(graph.nodes)
    if start != end:
        graph.addNode(Edge(start, end))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                addRandomPoint()
            elif event.key == pygame.K_e:
                addRandomEdge()

    pygame.display.flip()
    window.fill("white")

    graph.draw(window)

    deltaTime = clock.tick(fps)