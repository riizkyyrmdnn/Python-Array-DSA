# What is Insertion sort?

The origin of the word insert is insert which means inserting or inserting. So the insertion sort algorithm is an algorithm for sorting data by taking elements in an array, then the data will be inserted in the proper position.

## How it works

1. Data Sharing. The data is divided into two parts: the sorted left part and the unsorted right part.
2. Element Retrieval. The first element of the unsorted section is retrieved.
3. Comparison and Shift. The elements taken compared to the elements in the sorted section. If the captured element is smaller, the larger elements are shifted to the right to make room for the captured element.
4. Element Placement. The retrieved element is placed in the correct position inside the sorted part.
5. Iteration. Steps 2 through 4 are repeated for each element in the unsorted section.

## Example

Suppose we have a list of numbers: [3, 7, 1, 9, 5]

1. Iteration 1: The list is . The sorted part is , the unsorted part is [3, 7, 1, 9, 5][3][7, 1, 9, 5]
2. Iteration 2: Take 7. Since 7 is greater than 3, there is no need for a shift. Register as .[3, 7, 1, 9, 5]
3. Iteration 3: Take 1. 1 is smaller than 7, so swipe 7 to the right. Register as .[3, 1, 7, 9, 5]
4. Iteration 4: Take 9. Since 9 is greater than 7, there is no need for shifting. Register as .[3, 1, 7, 9, 5]
5. Iteration 5: Take 5. 5 is greater than 1 but smaller than 7, so slide 7 to the right and 1 to the right. Register as .[3, 1, 5, 7, 9]
6. After the last iteration, the list will be sorted: .[1, 3, 5, 7, 9]

## Excess

1. Simple to implement.
2. Efficient for near-sorted data.

## Deficiency

low for large, random data. The average time complexity is O(n^2).
