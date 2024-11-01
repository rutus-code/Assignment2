def quickSortAlgo(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[-1]
    smaller, larger = [], []

    for num in arr[:-1]:  # Exclude the pivot itself from the iteration
        if num < pivot: 
            smaller.append(num)
        else: 
            larger.append(num)
    
    return quickSortAlgo(smaller) + [pivot] + quickSortAlgo(larger)


#example 
arr = [5,6,2,95,35,10,3]
sorted_arr = quickSortAlgo(arr)
print('Original Array', arr)
print('Sorted Array', sorted_arr)