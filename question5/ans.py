arr = input("Enter array elements: ").split()
n = len(arr)
for i in range(n):
    for j in range(i, n):
        for k in range(i, j + 1):
            print(arr[k], end=' ')
        print()
    print()
