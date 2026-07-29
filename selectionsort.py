import time

# User Input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start_time = time.perf_counter()

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the minimum element with the current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# End Execution Time
end_time = time.perf_counter()

# Output
print("\nSorted Array:")
print(arr)

# Time Complexity
print("\nTime Complexity:")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")

# Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")