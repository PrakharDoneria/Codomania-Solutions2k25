### Formula:
\[
t_n = \frac{(-1)^n x^{2n+1}}{(2n+1)!}
\]
Where:
- \( n \) is the term number.
- \( x \) is the real number input.

### Python Program:

```python
import math

# Function to calculate nth term of the series
def term_of_series(x, n):
    return ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)

# Function to calculate the sum of first n terms of the series
def sine_series(n, x):
    sum_series = 0
    for i in range(n):
        sum_series += term_of_series(x, i)
    return sum_series

# Main program
def main():
    # Input from user
    try:
        n, x = map(float, input("Enter the values for n & x: ").split())
        n = int(n)  # Ensure n is an integer

        # Check if n is positive
        if n <= 0:
            print("Number of terms must be positive")
        else:
            # Calculate the sum of the series
            result = sine_series(n, x)
            print(f"Sum of the series at x = {x:.2f} with {n} terms is {result:.5f}")
    except ValueError:
        print("Invalid input, please enter valid values for n and x.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Input:** The program accepts two values, `n` (the number of terms) and `x` (the real number).
2. **Series Calculation:** It uses the formula for each term of the series and sums them up for `n` terms.
3. **Factorial:** The `math.factorial()` function is used to calculate the factorial of a number.
4. **Output:** The sum of the series is printed with 5 decimal places.

### Sample Input and Output:

**Test Case 1:**

Input:
```
Enter the values for n & x: 0 1.0
```

Output:
```
Number of terms must be positive
```

**Test Case 2:**

Input:
```
Enter the values for n & x: 5 0.5
```

Output:
```
Sum of the series at x = 0.50 with 5 terms is 0.47943
```

### Notes:
- The program checks if `n` is a positive integer. If not, it displays an error message.
- The sum is printed with 5 decimal places of precision.
