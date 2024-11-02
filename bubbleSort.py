# Created By : Rutu Shah
# Date : 31st October 2024
# Implementation of Bubble Sort for Part 2 of Assignment 2. 

'''
Bubble sort algorithm sorts an array from lowest value to highest value
'''
import time
import random
from memory_profiler import memory_usage  

# Bubble Sort function
def bubble_sort(myArray):
    n = len(myArray)
    for i in range(n - 1): 
        swapped = False
        for j in range(n - i - 1):
            if myArray[j] > myArray[j + 1]:
                myArray[j], myArray[j + 1] = myArray[j + 1], myArray[j]
                swapped = True
        if not swapped: 
            break
    return myArray      

# To measure time and memory, define measure_time function to capture start_time and end_time of the test cases defined datasets
def measure_time_and_memory(data):
    start_time = time.perf_counter()
    # To track the memory usage of bubble sort algo, we are using memory_usage function
    mem_usage = memory_usage((bubble_sort, (data,)))  
    end_time = time.perf_counter()
    return bubble_sort(data), end_time - start_time, max(mem_usage)  

# Main executable block
if __name__ == '__main__':
    my_array_to_sort = [53, 78, 90, 20, 74, 0, 56, 288, 32525, -138]

    # Datasets
    sorted_data = my_array_to_sort                
    reverse_sorted_data = sorted(my_array_to_sort, reverse=True)
    random_data = random.sample(range(-50, 50), 50)  

    # Test and print the results with example output
    print("Bubble Sort Performance on Different Datasets:")

    # Sorted array example
    sorted_result, sorted_time, sorted_memory = measure_time_and_memory(sorted_data[:])
    print(f"\nOriginal Sorted data: {sorted_data}")
    print(f"Sorted Result: {sorted_result}")
    print(f"Time taken: {sorted_time:.6f} seconds")
    print(f"Peak memory usage: {sorted_memory:.6f} MiB")  

    # Reverse sorted array example
    reverse_sorted_result, reverse_sorted_time, reverse_sorted_memory = measure_time_and_memory(reverse_sorted_data[:])
    print(f"\nOriginal Reverse sorted data: {reverse_sorted_data}")
    print(f"Sorted Result: {reverse_sorted_result}")
    print(f"Time taken: {reverse_sorted_time:.6f} seconds")
    print(f"Peak memory usage: {reverse_sorted_memory:.6f} MiB")  

    # Random data example
    random_result, random_time, random_memory = measure_time_and_memory(random_data[:])
    print(f"\nOriginal Random data: {random_data}")
    print(f"Sorted Result: {random_result}")
    print(f"Time taken: {random_time:.6f} seconds")
    print(f"Peak memory usage: {random_memory:.6f} MiB")
