# What is Counting sort?

Counting Sort is a non-comparative sorting technique in computer science. This algorithm works by counting the number of elements that have a certain value in an array, and uses a counting array to store the number of occurrences of each value. Counting Sort counts the occurrence of data and determines the index position of each object in the order of output.

## How it works

1. Define Range. Specify the maximum range (max) of the values in the array.
2. Create a Counter Array. Create an array of sizes and initialize all its elements with 0.countmax + 1
3. Count Occurrences. Iterations through the input array and for each element, increment. This means that it will store the number of occurrences in the input array.xcount[x]count[x]x
4. Change Counter Array. Modify it so that it stores the final position index of the elements in the output array.count[i]count[i]i
5. Create Output Array. Create an output array of the same size as the input array.
6. Fill Output Array. Iterate through the input array from the back. For each element, decrement and place on the index in the output array.xcount[x]xcount[x]

## Example

Suppose we have an array: [1, 4, 1, 2, 7, 4, 4, 0, 5, 1]

- Maximum range: 7
- Counter array: [0, 3, 1, 2, 3, 1, 0, 1]
- Change the counter array: [0, 3, 4, 6, 9, 10, 10, 11]
- Array output: [0, 1, 1, 1, 2, 4, 4, 4, 5, 7]

## Advantage

1. Highly efficient for data with small value ranges.
2. Stable (does not change the order of elements that have the same value).

## Deficiency

1. Inefficient for data with large value ranges.
2. Requires additional memory for the counter array.
