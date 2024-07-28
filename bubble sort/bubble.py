def bubble_sort(array):
    if not array:
        return []
    
    for i in range(len(array)):
        swap = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                element = array[j]
                array[j] = array[j + 1]
                array[j + 1] = element
                swap = True
        if not swap:
            break
    return array

def switch(choice):
    if choice == 1:
        print("__Sorting array integer__")
        int_array = [88, 91, 54, 61, 73, 81, 65, 71, 90, 99, 64, 83, 85, 61, 46, 29, 11, 28, 12, 71, 83, 32, 64, 97, 17, 25, 16, 89]
        print(f"Before sort: {int_array}")
        print(f"After sort: {bubble_sort(int_array)}")
    elif choice == 2:
        print("__Sorting array float__")
        float_array = [8.4, 9.1, 3.9, 8.2, 4.89, 1.25, 1.8, 9.87, 7.68, 96.51, 78.8, 6.1, 6.8, 1.09, 4.2, 9.91, 10.0, 1.3, 2.8, 3.9, 1.1, 8.56, 7.12]
        print(f"Before sort: {float_array}")
        print(f"After sort: {bubble_sort(float_array)}")
    elif choice == 3:
        print("__Sorting array string__")
        string_array = ["hello", "you", "string", "int", "double", "unsigned", "floating", "float", "array", "long", "world", "classes", "enumirate", "byte"]
        print(f"Before sort: {string_array}")
        print(f"After sort: {bubble_sort(string_array)}")
    else:
        print("0. Close program\n")


if __name__ == "__main__":
    print("___ Bubble Sort ___")
    print("1. Sorting array integer")
    print("2. Sorting array float")
    print("3. Sorting array string")
    print("0. Close program\n")

    choice = int(input("> Your choice: "))

    print(f"\nYour choice is: {choice}")
    switch(choice)