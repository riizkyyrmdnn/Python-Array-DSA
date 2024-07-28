def max_value(iterable):
    if len(iterable) == 0:
        raise ValueError("check iterable is not empty")
    _max = iterable[0]
    for index in iterable[1:]:
        if index > _max:
            _max = index
    return _max

def min_value(iterable):
    if len(iterable) == 0:
        raise ValueError("check iterable is not empty")
    _min = iterable[0]
    for index in iterable[1:]:
        if index < _min:
            _min = index
    return _min

def search_int():
    int_array = [88, 91, 54, 61, 73, 81, 65, 71, 90, 99, 64, 83, 85, 61, 46, 29, 11, 28, 12, 71, 83, 32, 64, 97, 17, 25, 16, 89]
    print(f"> Smallest Integer Array Value: {min_value(int_array)}")
    print(f"> Largest Integer Array Value: {max_value(int_array)}")

def search_float():
    float_array = [8.4, 9.1, 3.9, 8.2, 4.89, 1.25, 1.8, 9.87, 7.68, 96.51, 78.8, 6.1, 6.8, 1.09, 4.2, 9.91, 10.0, 1.3, 2.8, 3.9, 1.1, 8.56, 7.12]
    print(f"> Smallest Float Array Value: {min_value(float_array)}")
    print(f"> Largest Float Array Value: {max_value(float_array)}")

def search_string():
    string_array = ["hello", "you", "string", "int", "double", "unsigned", "floating", "float", "array", "long", "world", "classes", "enumirate", "byte"]
    print(f"> Smallest String Array Value: {min_value(string_array)}")
    print(f"> Largest String Array Value: {max_value(string_array)}")

def switch(choice):
    if choice == 1:
        print("\nFind the integer array type with the smallest and largest values.\n")
        search_int()
    elif choice == 2:
        print("\nFind the float array type with the smallest and largest values.\n")
        search_float()
    elif choice == 3:
        print("\nLooking for the type of string array with the smallest and largest value (based on the initial character)\n")
        search_string()
    else:
        print("You end the program.")

if __name__ == "__main__":
    print("___ Find the smallest and largest value ___")
    print("1. Array Integer")
    print("2. Array Float")
    print("3. Array String")
    print("0. Close program\n")

    choice = int(input("> Your choice: "))

    print(f"\nYour choice is: {choice}")
    switch(choice)
