array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(array)

def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >=pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

def quick_sort(arr, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
