import time

# User Input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start_time = time.perf_counter()

# Optimized Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    # If no swaps occurred, array is already sorted
    if not swapped:
        break

# End Execution Time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

# Time Complexity
print("\nTime Complexity:")
print("Best Case   : O(n)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")

# Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")
