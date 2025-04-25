# Question: Print Subarrays

Write a program to print all the subarrays of a given array. For each element in the array, print the subarray starting from that element to the end of the array.

## Input
- A list of integers.

## Output
- Print each subarray starting from each element to the end of the array.

## Sample Input
```
[2, 4, 6, 8]
```

## Sample Output
```
2
2 4
2 4 6
2 4 6 8

4
4 6
4 6 8

6
6 8

8
```

## Explanation
For the input array `[2, 4, 6, 8]`, the program prints the following subarrays:

1. The subarrays starting from `2` are: `[2]`, `[2, 4]`, `[2, 4, 6]`, `[2, 4, 6, 8]`
2. The subarrays starting from `4` are: `[4]`, `[4, 6]`, `[4, 6, 8]`
3. The subarrays starting from `6` are: `[6]`, `[6, 8]`
4. The subarray starting from `8` is: `[8]`

## Constraints
- The array contains non-negative integers.