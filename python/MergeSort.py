#use over quicksort when dataset is large and on external device (less disk writes) or if need to guarantee time complexity

import math

def combineArr(arr, l, r):
    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
       if l[i] < r[j]:
           arr[k] = l[i]
           i = i + 1
       else:
           arr[k] = r[j]
           j = j + 1
       k = k + 1

    while i < len(l):
       arr[k] = l[i]
       i = i + 1
       k = k + 1

    while j < len(r):
       arr[k] = r[j]
       j =j + 1
       k = k + 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = math.floor(len(arr)/2)
        lArr = arr[:mid]
        rArr = arr[mid:]

        mergeSort(lArr)
        mergeSort(rArr)

        combineArr(arr, lArr, rArr)

sortArray = [8, 2, 17, 14, 99, 44, 20]
mergeSort(sortArray)
print(sortArray)