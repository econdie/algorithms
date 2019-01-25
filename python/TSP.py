import math
def calcRoute(graph, startingNode):
    unvisited = set(graph.keys())
    path = []
    distance = 0
    currentNode = startingNode
    unvisited.remove(currentNode)
    while unvisited:
        minDistance = math.inf
        nextNode = None
        for node, weight in graph[currentNode].items():
            if weight < minDistance and node in unvisited:
                minDistance = weight
                nextNode = node

        unvisited.remove(nextNode)
        path.append(nextNode)
        distance = distance + minDistance
        currentNode = nextNode
    distance = distance + graph[currentNode][startingNode]
    path.append(startingNode)
    print('calced distance ' + str(distance))
    print('calced path ' + str(path))


graph = {'a': {'b': 7, 'c': 10, 'd': 5, 'e': 20, 'f': 9}, 'b': {'a': 7, 'c': 15, 'd': 15, 'e': 4, 'f': 11}, 'c': {'a': 10, 'b': 15, 'd': 22, 'e': 14, 'f': 5}, 'd': {'a': 5, 'b': 15, 'c': 22, 'e': 7, 'f': 10}, 'e': {'a': 20, 'b': 4, 'c': 14, 'd': 7, 'f': 25}, 'f': {'a': 9, 'b': 11, 'c': 5, 'd': 10, 'e': 25}}
calcRoute(graph, 'a')

# import itertools
# for item in itertools.permutations(graph.keys()):
#     print(item)