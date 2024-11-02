# Created By : Rutu Shah
# Date : 31st October 2024
# Implementation of Heap Sort for Part 2 of Assignment 2. 

import time
import random
from memory_profiler import memory_usage  # Make sure to install this package

def heapsort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def measure_time_and_memory(data):
    start_time = time.perf_counter()
    # Measure memory usage while running heapsort
    mem_usage = memory_usage((heapsort, (data,)))  
    end_time = time.perf_counter()
    return heapsort(data), end_time - start_time, max(mem_usage)  

# Main executable block
if __name__ == '__main__':
    my_array_to_sort = [53, 78, 90, 20, 74, 0, 56, 288, 32525, -138]

    # Datasets
    sorted_data = my_array_to_sort                
    reverse_sorted_data = sorted(my_array_to_sort, reverse=True)
    random_data = random.sample(range(-50, 50), 50)  

    # Test and print the results
    print("Heap Sort Performance on Different Datasets:")

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
