a = [1,4,3,8,7,4,10,2]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j+1],a[j] = a[j], a[j+1]

print(a)
