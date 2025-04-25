def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))
ncr = factorial(n) // (factorial(r) * factorial(n - r))
print(ncr)