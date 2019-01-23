##ideal for array that is already almost sorted

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j = j - 1

sortArray = [8, 2, 17, 14, 99, 44, 20]
insertionSort(sortArray)
print(sortArray)