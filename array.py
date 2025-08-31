import array

def main():
    # Create an array of integers
    int_array = array.array('i', [1, 2, 3, 4, 5])
    int_array_2 = array.array('i', [7, 8, 9, 10])
    
    # Print the original array
    print("Original array:", int_array)

    # Print the second array
    print("Original array 2:", int_array_2)
    
    # Append a new integer to the array
    int_array.append(6)
    print("Array after appending 6:", int_array)

    # Extend the array with another array
    int_array.extend(int_array_2)
    print("Array after extending with int_array_2:", int_array)

    int_array.index(4)
    print("Index of element 4:", int_array.index(4))
    
    # Remove an element using the element from the array
    int_array.remove(3)
    print("Array after removing 3:", int_array)

    # Remove an element using its index
    int_array.pop(1)  
    print("Array after popping index 1:", int_array)
    
    # Access an element by index
    print("Element at index 2:", int_array[2])

    #Reverse the array
    #int_array.reverse()
    print("Reversed array:", int_array[::-1])

    # Add multiple elements using fromlist
    int_array += array.array('i', [11, 12, 13])
    print("Array after adding [11, 12, 13]:", int_array)

    int_array *= 2
    print("Array after multiplying by 2:", int_array)

    # Convert array to list
    int_list = int_array.tolist()   
    print("Array converted to list:", int_list)

main()