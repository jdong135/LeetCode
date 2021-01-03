a = [3,4,5,6,7,8,8,8,8,9,0,0,1,1]
# Find 1) Pivot point
left = 0
right = len(a) - 1
while left < right:
    mid = (left + right) // 2
    if a[mid] <= a[right]:
        right = mid
    else:
        left = mid + 1
print("Index of pivot: " + str(left))

# Find 2) Max Value
left = 0
right = len(a) - 1
while left < right:
    mid = (left + right) // 2
    if a[mid] > a[mid + 1]:
        left = mid
        break
    elif a[mid] <= a[right]:
        right = mid - 1
    else:
        left = mid
print("Max value: " + str(a[left]))
