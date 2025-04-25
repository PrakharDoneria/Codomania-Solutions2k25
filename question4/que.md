# Question: Binomial Coefficient (nCr)

Write a program to calculate the binomial coefficient \( nCr \) using the formula:

\[
nCr = \frac{n!}{r!(n - r)!}
\]

Where:
- \( n! \) is the factorial of \( n \)
- \( r! \) is the factorial of \( r \)
- \( (n - r)! \) is the factorial of \( (n - r) \)

## Input
- Two integers \( n \) and \( r \) where \( n \geq r \).

## Output
- The binomial coefficient \( nCr \).

## Sample Input 1
```
n = 5
r = 2
```

## Sample Output 1
```
The value of 5C2 is: 10
```

## Sample Input 2
```
n = 6
r = 3
```

## Sample Output 2
```
The value of 6C3 is: 20
```

## Explanation
- For the first example, the binomial coefficient is \( 5C2 = \frac{5!}{2!(5-2)!} = \frac{5!}{2!3!} = \frac{120}{2 \times 6} = 10 \).
- For the second example, the binomial coefficient is \( 6C3 = \frac{6!}{3!(6-3)!} = \frac{720}{6 \times 6} = 20 \).

## Constraints
- \( n \) and \( r \) are non-negative integers.
- \( n \geq r \).