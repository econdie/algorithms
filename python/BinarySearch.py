import math

def binarySearch(arr, l, r, target):
    if r >= 1 and r >= l:
        mid = math.floor(l + (r - l)/2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarySearch(arr, mid+1, r, target)
        else:
            return binarySearch(arr, l, mid-1, target)
    else:
        return 'invalid'

arr = [2, 3, 4, 10, 40]
x = 10
print(binarySearch(arr, 0, len(arr) - 1, x))
