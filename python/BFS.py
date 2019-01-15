graph = [[0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0]]

queue = [0]
visited = [0]

while len(queue) > 0:
    node = queue.pop()
    for key, value in enumerate(graph[node]):
        if value == 1 and key not in visited:
            visited.append(key)
            queue.insert(0, key)

for node in visited:
    print(node)