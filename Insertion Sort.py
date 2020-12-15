arr = [38, 27, 43, 3, 9, 82, 10]
print(arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and key < arr[j]:
        # Shifting greater elements one upwards
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = key

print(arr)
        
