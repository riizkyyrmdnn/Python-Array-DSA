def quicksort(array, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)

    return array

def switch(choice):
    if choice == 1:
        print("__Sorting array integer__")
        int_array = [88, 91, 54, 61, 73, 81, 65, 71, 90, 99, 64, 83, 85, 61, 46, 29, 11, 28, 12, 71, 83, 32, 64, 97, 17, 25, 16, 89]
        print(f"Before sort: {int_array}")
        print(f"After sort: {quicksort(int_array)}")
    elif choice == 2:
        print("__Sorting array float__")
        float_array = [8.4, 9.1, 3.9, 8.2, 4.89, 1.25, 1.8, 9.87, 7.68, 96.51, 78.8, 6.1, 6.8, 1.09, 4.2, 9.91, 10.0, 1.3, 2.8, 3.9, 1.1, 8.56, 7.12]
        print(f"Before sort: {float_array}")
        print(f"After sort: {quicksort(float_array)}")
    elif choice == 3:
        print("__Sorting array string__")
        string_array = ["hello", "you", "string", "int", "double", "unsigned", "floating", "float", "array", "long", "world", "classes", "enumirate", "byte"]
        print(f"Before sort: {string_array}")
        print(f"After sort: {quicksort(string_array)}")
    else:
        print("0. Close program\n")


if __name__ == "__main__":
    print("___ Quicksort ___")
    print("1. Sorting array integer")
    print("2. Sorting array float")
    print("3. Sorting array string")
    print("0. Close program\n")

    choice = int(input("> Your choice: "))

    print(f"\nYour choice is: {choice}")
    switch(choice)