##ideal for not a lot of resources for disk writing
def selectionSort(arr):
    index = 0
    
    for index in range(0, len(arr) - 1):
        smallest = None
        smallestIndex = None
        for i in range(index, len(arr)):
            if smallest is None or arr[i] < smallest:
                smallest = arr[i]
                smallestIndex = i
        temp = arr[index]
        arr[index] = smallest
        arr[smallestIndex] = temp

sortArray = [8, 2, 17, 14, 99, 44, 20]
selectionSort(sortArray)
print(sortArray)
