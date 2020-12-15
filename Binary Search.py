arr = [3, 9, 10, 27, 38, 43, 82]

def binary_iterative(arr, num):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1

def binary_recursive(arr, low, high, num):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binary_recursive(arr, mid+1, high, num)
        elif arr[mid] > num:
            return binary_recursive(arr, low, mid-1, num)
    else:
        return -1

print(binary_iterative(arr, 9))
print(binary_iterative(arr, 100))
print(binary_recursive(arr, 0, len(arr)-1, 9))
print(binary_recursive(arr, 0, len(arr)-1, 100))
            
