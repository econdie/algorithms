def partition(sortArray, low, high):
    index = low-1
    pivot = sortArray[high]

    for j in range(low, high):
        if sortArray[j] <= pivot:
            index = index + 1
            temp = sortArray[j]
            sortArray[j] = sortArray[index]
            sortArray[index] = temp
        

    index = index + 1
    temp = sortArray[index]
    sortArray[index] = sortArray[high]
    sortArray[high] = temp
    return index

def quickSort(sortArray, low, high):
    if (low < high):
        pIndex = partition(sortArray, low, high)
        quickSort(sortArray, low, pIndex-1)
        quickSort(sortArray, pIndex+1, high)

sortArray = [10, 7, 8, 9, 1, 5]
quickSort(sortArray, 0, len(sortArray)-1)
for element in sortArray:
    print(element)
