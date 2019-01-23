#use over mergesort when sorting done in memory

def getPartitionIndex(arr, l, r):
    index = l - 1
    pivotVal = arr[r]
    for i in range(l, r):
        if arr[i] <= pivotVal:
            index = index + 1
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp

    index = index + 1
    arr[r] = arr[index]
    arr[index] = pivotVal
    return index

def quickSort(arr, l, r):
    if l < r:
        pIndex = getPartitionIndex(arr, l, r)
        quickSort(arr, l, pIndex - 1)
        quickSort(arr, pIndex+1, r)

sortArray = [8, 2, 17, 14, 99, 44, 20]
quickSort(sortArray, 0, len(sortArray) - 1)
print(sortArray)
