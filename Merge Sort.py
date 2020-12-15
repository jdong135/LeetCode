arr = [38, 27, 43, 3, 9, 82, 10]
print(arr)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergesort(left)
        mergesort(right)
        
        # Once the len(arr) == 1, the mergsesorts will stop and merging starts
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

mergesort(arr)
print(arr)
