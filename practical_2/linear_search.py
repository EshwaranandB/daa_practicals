import time


def linear_search(arr, target):
    """
    Performs Linear Search by checking each element sequentially.
    Returns index if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return its index
    return -1  # Target not found


def main():
    # Take list input from user
    raw_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    numbers = [int(x) for x in raw_input.split()]

    # Take target value input
    target = int(input("Enter the target number to search: "))

    # Measure execution time
    start_time = time.perf_counter()
    result_index = linear_search(numbers, target)
    end_time = time.perf_counter()

    execution_time_ms = (end_time - start_time) * 1000

    print("\n--- Results ---")
    if result_index != -1:
        print(f"Target {target} found at index: {result_index}")
    else:
        print(f"Target {target} was not found in the list.")

    print(f"Execution Time: {execution_time_ms:.6f} ms")


if __name__ == "__main__":
    main()
