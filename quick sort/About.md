# What is Quick sort?

The Quick Sort algorithm is an efficient and popular method of sorting data in computer science. The working principle is based on the "Break and Conquer" method, where the data to be sorted is partitioned into two parts, then the parts are sorted separately, and finally recombined.

## How it works?

1. Pivot Selection. An element of the array is selected as a pivot.
2. Partitions. The elements of the array are divided into two parts based on pivot values:
   - The smaller element of the pivot is placed to the left of the pivot.
   - The larger element of the pivot is placed to the right of the pivot.
3. Recursion. The process is repeated recursively for the sub-arrays to the left and right of the pivot until the entire array is sorted.

## Advantage

1. Efficient. Quick Sort generally performs well, especially on random data.
2. In-place. Doesn't require significant additional memory.

## Deficiency

Worst Performance: In certain cases, such as sorted data, Quick Sort's performance can degrade drastically.
