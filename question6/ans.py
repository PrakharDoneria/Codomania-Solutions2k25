import math

def sin_series(n, x):
    sum_terms = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sum_terms += term
    return sum_terms

n, x = map(float, input("Enter the values for n & x: ").split())
n = int(n)

if n <= 0:
    print("Number of terms must be positive")
else:
    result = sin_series(n, x)
    print(f"Sum of the series at x = {x} with {n} terms is {result:.5f}")