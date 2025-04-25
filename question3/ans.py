def count_ways(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter the value of n: "))
print(count_ways(n))
