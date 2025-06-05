if mazeScanned and not graphTrimed:
        for node in graph.nodes:
            n = graph.getNeighbors(node)
            if len(n) == 1 and not (node.equals(start) or node.equals(end)):
                graph.removeNode(node)