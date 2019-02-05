# build systems
# advanced packaging tool
# task scheduling
# pre requisite problems

def traverse(graph, node, unvisited, nodeStack):
    if node in unvisited:
        unvisited.remove(node)
    for childNode in graph[node]:
        if childNode in unvisited:
            traverse(graph, childNode, unvisited, nodeStack)

    nodeStack.insert(0, node)

def topologicalSort(graph):
    unvisited = set(graph.keys())
    nodeStack = []

    while unvisited:
        node = unvisited.pop()
        traverse(graph, node, unvisited, nodeStack)

    return nodeStack

graph = {'a': {'b', 'f'}, 'b': {'h'}, 'c': {}, 'd':{'c', 'e', 'i'}, 'e':{'i'}, 'f':{}, 'g':{'a', 'b', 'c'}, 'h':{}, 'i':{'c'}, 'j':{'e'}}
topSort = topologicalSort(graph)
print(topSort)