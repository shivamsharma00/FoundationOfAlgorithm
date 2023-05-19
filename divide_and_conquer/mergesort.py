import time
import random
import math

def mergesort(unsorted_array):
    # Get the length of the array
    arr_len = len(unsorted_array)

    # Calculate the midpoint of the array
    mid = int(arr_len/2 if arr_len%2==0 else arr_len/2+1)

    # Split the array into two halves
    first_half = unsorted_array[0:mid]
    second_half = unsorted_array[mid:]

    # Sort the two halves separately
    first_half = sorted(first_half)
    second_half = sorted(second_half)

    # Get the lengths of the two halves
    len_fh = len(first_half)
    len_sh = len(second_half)

    # Initialize variables
    sorted_array = []
    first_counter = 0
    second_counter = 0

    # Merge the two sorted halves into a single sorted array
    for i in range(arr_len):
        if first_counter < len_fh:
            if second_counter < len_sh:
                if first_half[first_counter] < second_half[second_counter]:
                    sorted_array.append(first_half[first_counter])
                    first_counter += 1
                else:
                    sorted_array.append(second_half[second_counter])
                    second_counter += 1
            else:
                sorted_array.append(first_half[first_counter])
                first_counter += 1
        elif second_counter < len_sh:
            sorted_array.append(second_half[second_counter])
            second_counter += 1

    return sorted_array

if __name__ == "__main__":
    # Generate a random list of numbers
    l = []
    r = 1000000
    for i in range(r):
        l.append(random.randint(1, 2000))

    s = time.time()
    # Call mergesort function to sort the list
    sorted_array = mergesort(l)
    e = time.time()

    # Print the execution time
    print("Execution Time: " + str(e-s) + " seconds")

    # Calculate the computation time complexity
    c_t = r*(math.log2(r))
    print("Computation Time O(nlog(n)): " + str(c_t))
