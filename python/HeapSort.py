#not stable
#maintaining heap requires resource
#quicksort has lower constant factor than heapsort
import math

def heapify(arr, index):
    root = index
    swapped = False
    try:
        if arr[root * 2 + 1] > arr[root]:
            temp = arr[root * 2 + 1]
            arr[root * 2 + 1] = arr[root]
            arr[root] = temp
            swapped = True
    except:
        pass
    try:
        if arr[root * 2 + 2] and arr[root * 2 + 2] > arr[root]:
            temp = arr[root * 2 + 2]
            arr[root * 2 + 2] = arr[root]
            arr[root] = temp
            swapped = True
    except:
        pass

    if swapped:
        try:
            if arr[(root * 2 + 1)*2 + 1]:
                heapify(arr, (root * 2 + 1))
        except:
            pass


def heapSort(arr):
    ##O(n)
    for i in range(math.floor((len(arr)-2)/2), -1, -1):
        heapify(arr, i)

    sortedArr = []
    for i in range(len(arr) - 1, 0, -1):
        sortedVal = arr[0]
        sortedArr.insert(0, sortedVal)
        arr[0] = arr.pop()
        heapify(arr, 0)

    sortedArr.insert(0, arr.pop())
    return sortedArr

sortArray = [8, 2, 17, 14, 99, 44, 20]
sortedArray = heapSort(sortArray)
print(sortedArray)
