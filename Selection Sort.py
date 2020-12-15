arr = [38, 27, 43, 3, 9, 82, 10]
print(arr)

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    # Swap the found minimum element with the first element  
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
print(arr)
