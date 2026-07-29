import time

# Function to perform partition
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start_time = time.perf_counter()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# End Execution Time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

# Time Complexity
print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n²)")

# Space Complexity
print("\nSpace Complexity:")
print("Average Case: O(log n)")
print("Worst Case  : O(n)")

# Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")