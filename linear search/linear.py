def linear_search(array, number, target):
    for i in range(0, number):
        if array[i] == target:
            return i
    return -1

if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]
    print("\n___Linear search___\n")
    target = int(input("> The value you want to find: "))
    result = linear_search(array, len(array), target)
    if result != -1:
        print(f"> Index of the target: {result}")
    else:
        print("Target not found")