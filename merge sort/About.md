# What is Merge sort?

Merge sort is a sorting algorithm in computer science that utilizes the "divide and conquer" technique. This algorithm is designed to sort data sets that cannot be accommodated in computer memory due to their excessive volume. Merge sort was invented by John von Neumann in 1945.

## How it works

1. Divide. The list is divided into two equal parts recursively until each part contains only one element.
2. Conquer. Two sorted sub-lists are combined into a single sorted list by comparing the elements of the two sub-lists alternately.
3. Repeat. This process continues until the entire list is sorted.

## Example

Suppose we have a list of numbers: [38, 27, 43, 3, 9, 82, 10]

## Division

- [38, 27, 43, 3] and [9, 82, 10]
- [38, 27], and ,[43, 3][9, 82] [10]
- [38], , , , , ,[27][43][3][9][82] [10]

## Merging:

- [27, 38], ,[3, 43] [9, 82]
- [3, 27, 38, 43], [9, 82]
- [3, 9, 27, 38, 43, 82]

## Final merger

[3, 9, 10, 27, 38, 43, 82]

## Advantage

Efficiency. Has O(n log n) time complexity in all cases.
Stable. Doesn't change the order of elements that have the same value.

## Deficiency

Requires additional memory to store temporary sub-lists.
