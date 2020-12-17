arr = [-2, 2, 5, -11, 6]

def kadane(arr):
    max_sum = arr[0]
    current_sum = max_sum
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(kadane(arr))
