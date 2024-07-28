# What is Bubble Sort

Bubble sort is a sorting algorithm that works by comparing or swapping pairs of adjacent elements in an array when they are in an incompatible order. The process of swapping and benchmarking is carried out from the beginning of the array to the end. This algorithm can sort data from large to small (ascending) or small to large (descending).

## How it works

1. Comparison. The elements in the list are compared in pairs.
2. Swap. If two consecutive elements are not in the desired order (for example, in ascending order, the first element is greater than the second), then they are swapped positions.
3. Iteration. This process is repeated continuously until no more redemptions occur in a single iteration, which means the list has been sorted.

## Example

Suppose we have a list of numbers: [64, 34, 25, 12, 22, 11, 90]

- 64 compared to 34, exchanged: [34, 64, 25, 12, 22, 11, 90]
- 64 compared to 25, exchanged: [34, 25, 64, 12, 22, 11, 90]
- ... and so on
After a few iterations, the list will be sorted: [11, 12, 22, 25, 34, 64, 90]

## Debilitation

Efficiency. Bubble Sort is a slow algorithm, especially for large lists. The time complexity is O(n^2) in the worst case.
