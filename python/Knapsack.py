def buildKnapsack(items, index, capacity, K):
    if K[index][capacity] is not None:
        return K[index][capacity]
    elif index < 0 or capacity <= 0:
        result = 0
    elif items[index][0] > capacity:
        result = buildKnapsack(items, index - 1, capacity, K)
    else:
        result = max(buildKnapsack(items, index - 1, capacity, K), items[index][1] + buildKnapsack(items, index - 1, capacity - items[index][0], K))
    K[index][capacity] = result
    return result

items = [(5, 7), (3, 4), (4, 5), (4, 9), (1,3), (10, 3), (5, 5)]
K = [[None for c in range(11)] for i in range(len(items))]
print(buildKnapsack(items, len(items)-1, 10, K))
print(K)
w = 10
knapsack = set()
res = K[len(items)-1][w]
for i in range(len(items)-1, -1, -1):
    if i == 0:
        if items[i][0] <= w:
            knapsack.add(items[i])
    if K[i][w] - K[i-1][w-items[i][0]] == items[i][1]:
        knapsack.add(items[i])
        w = w - items[i][0]

print(knapsack)