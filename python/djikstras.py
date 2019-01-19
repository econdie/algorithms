import math

def djikstras(graph, start, target):
    minDistances = {}
    previousNodes = {}
    unvisitedNodes = set(graph.keys())
    
    path = []
    for node in unvisitedNodes:
        if node == start:
            minDistances[node] = 0
        else:
            minDistances[node] = math.inf

    while unvisitedNodes:
        minNode = None
        for node in unvisitedNodes:
            if minNode == None:
                minNode = node
            elif minDistances[node] < minDistances[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if minDistances[minNode] + weight < minDistances[childNode]:
                minDistances[childNode] = minDistances[minNode] + weight
                previousNodes[childNode] = minNode

        unvisitedNodes.remove(minNode)

    pathNode = target
    while pathNode != start:
        try:
            path.insert(0, pathNode)
            pathNode = previousNodes[pathNode]
        except KeyError:
            print('invalid path')
            break
    path.insert(0, start)

    if minDistances[target] != math.inf:
        print('shortest path: ' + str(path))
        print('shortest path distance: ' + str(minDistances[target]))



graph = {'a': {'b':10, 'c':3}, 'b':{'c':1,'d':2}, 'c':{'b':4, 'd':8, 'e':2}, 'd':{'e':7}, 'e':{'d':9}}
djikstras(graph, 'a', 'd')
