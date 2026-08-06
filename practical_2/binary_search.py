import time


def binary_search(arr, target):
    """
    Performs Binary Search using a divide-and-conquer strategy.
    Assumes array is sorted in ascending order.
    Returns index if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found


def main():
    # Take list input from user
    raw_input = input("Enter numbers separated by spaces (e.g., 10 20 30 40 50): ")
    numbers = [int(x) for x in raw_input.split()]

    # Binary search requires sorted data
    sorted_numbers = sorted(numbers)
    print(f"\nSorted List for Binary Search: {sorted_numbers}")

    # Take target value input
    target = int(input("Enter the target number to search: "))

    # Measure execution time
    start_time = time.perf_counter()
    result_index = binary_search(sorted_numbers, target)
    end_time = time.perf_counter()

    execution_time_ms = (end_time - start_time) * 1000

    print("\n--- Results ---")
    if result_index != -1:
        print(f"Target {target} found at index: {result_index} (in sorted array)")
    else:
        print(f"Target {target} was not found in the list.")

    print(f"Execution Time: {execution_time_ms:.6f} ms")


if __name__ == "__main__":
    main()
