# What is Linear search?

Linear search is a search algorithm that visits each element in an array or list individually. If the searched value is found, the algorithm will return the output; Otherwise, the search will continue to the end of the array or list.

## How it works

1. Start with the first element on the list.
2. Compare the current element to the value you are looking for.
3. If an element is found, return the index.
4. If an element is not found, proceed to the next element.
5. Repeat steps 2 through 4 to the end of the list.
6. If the element is not found after checking the entire list, return a value that indicates not found (usually -1).

## Example

Suppose we have a list of numbers: and want to find the number 5.[3, 7, 1, 9, 5]

- Start from the first element: 3. Not suitable.
- Continue to the second element: 7. Not suitable.
- Continue to the third element: 1. Not suitable.
- Continue to the fourth element: 9. Not suitable.
- Continue to the fifth element: 5. Match, return index 4.

## Advantages and Disadvantages

1. Pros: Simple to implement.
2. Cons: Slow for large lists, especially if the searched element is at the end of the list. The time complexity is O(n), where n is the number of elements in the list.
