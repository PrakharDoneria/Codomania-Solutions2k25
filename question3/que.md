# Question: Tiling Problem

Given a floor of size "2 * n" and tiles of size "2 * 1", count the number of ways to tile the given floor using the 2 * 1 tiles.

## Problem Description

You have a "2 * n" floor, and you are provided with tiles of size "2 * 1". You need to determine the number of ways to completely tile the given floor using these tiles. The tiles can be placed either vertically or horizontally.

## Input
- A single integer `n` representing the length of the floor.

## Output
- The number of ways to tile the floor using "2 * 1" tiles.

## Sample Input 1
```
n = 3
```

## Sample Output 1
```
3
```

## Sample Input 2
```
n = 4
```

## Sample Output 2
```
5
```

## Explanation

For `n = 3`, the possible ways to tile the floor are:

1. All tiles placed vertically.
2. Two tiles placed horizontally (in two rows) and one tile placed vertically.
3. One tile placed horizontally in the first row, another in the second row, and the third tile placed vertically.

Hence, there are 3 ways to tile the floor.

For `n = 4`, the possible ways to tile the floor are:

1. All tiles placed vertically.
2. Two sets of two tiles placed horizontally (in two rows).
3. A mix of vertical and horizontal tile placements.

Hence, there are 5 ways to tile the floor.

## Constraints
- The input `n` is a positive integer.
