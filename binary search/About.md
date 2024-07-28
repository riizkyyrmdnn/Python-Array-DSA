# What is binary search?

Binary search is an algorithm used to search for certain elements in a sorted data set. This algorithm works by dividing the dataset into two parts, then checking whether the element being searched is located on the left or right. Binary search assumes that the data is already sorted, whether it is in ascending or descending order.

## How it works

1. Data Sharing. The list is divided into two equal sections.
2. Comparison. The middle element of the list is compared to the element being searched.
3. Part Determination:
   - If the middle element is the same as the element being sought, the search is complete.
   - If the element being searched is smaller than the middle element, the search continues on the left side of the list.
   - If the element being searched is larger than the middle element, the search continues on the right side of the list.
4. Repetition. Steps 1 through 3 are repeated recursively or iteratively until an element is found or not found.

## Advantages of Binary Search

- Efficiency. Has O(log n) time complexity, which means the larger the data, the faster the search will be performed.
- Speed. Very fast for large lists.

## Limitations

- Sorted Data. Can only be used on sorted data.
- Iteration. Requires multiple iterations to find an element.

## Usage Examples

- Look up words in the dictionary
- Find a value in a database table
- Finding elements in an ordered array
