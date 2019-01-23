def bubbleSort(arr):
    isSorted = False
    while not isSorted:
        for i in range(0, len(arr) - 1):
            isSorted = True
            if arr[i] > arr[i+1]:
                isSorted = False
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

sortArray = [8, 2, 17, 14, 99, 44, 20]
bubbleSort(sortArray)
print(sortArray)
