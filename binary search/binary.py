# iterative
def binary_search_iterative(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# recursive
def binary_search_recursive(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, low, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, high)

def switch(choice):
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]
    
    if choice == 1:
        print("\n__Binary search with iterative__\n")
        target = int(input("> The value you want to find: "))
        print(f"> Index of the target: {binary_search_iterative(array, target)}")
    elif choice == 2:
        print("\n__Binary search with recursive__\n")
        target = int(input("> The value you want to find: "))
        print(f"> Index of the target: {binary_search_recursive(array, target, 0, len(array) - 1)}")
    else:
        print("You end the program.")

if __name__ == "__main__":
    print("___ Binary search with iterative and recursive __")
    print("1. Binary search iterative")
    print("2. Binary search Recursive")
    print("0. Close program\n")

    choice = int(input("> Your choice: "))

    print(f"\nYour choice is: {choice}")
    switch(choice)