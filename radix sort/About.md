# What is Radix sort?

Radix Sort is a non-comparative sorting algorithm that works by grouping individual digits of an element to be sorted. This is different from other sorting algorithms such as Quick Sort or Merge Sort that compare elements directly.

## How it works

1. Identify the rightmost digit. Specify the rightmost digit to use for the first grouping.
2. Group formation. The elements are divided into groups based on the rightmost digit value.
3. Repeat. The grouping process is repeated for the next digit, from right to left.
4. Merging. Once all the digits have been processed, the elements will be sorted.

## Example

Suppose we want to sort the numbers: [170, 45, 75, 90, 802, 24, 2, 66]

1. Grouping by unit digits:
   - 170, 90, 802, 2
   - 45, 75, 24, 66

2. Grouping by tens digits:
   - 2, 24
   - 45, 75, 90
   - 170, 802

3. Grouping by hundredth digits: [2, 24, 45, 66, 75, 90, 170, 802]

## Advantage

1. Efficient for data with a limited range of values.
2. It does not require direct comparison between elements.

## Deficiency

1. Suboptimal performance for data with very large value ranges.
2. Implementations can be more complex than other sequencing algorithms.
