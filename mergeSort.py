#Created By : Rutu Shah
#Date : 31st October 2024
# Merge Sort Algorithm code, this is for part 1 of Assignment 2

def merge_sort(arr):
    # Base case: if the list is of length 1 or empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left, add them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example 
if __name__ == "__main__":
    data = [53, 78, 90, 20, 74, 0, 56, 288, 32525, -138]
    sorted_data = merge_sort(data)
    print("Sorted Result:", sorted_data)
