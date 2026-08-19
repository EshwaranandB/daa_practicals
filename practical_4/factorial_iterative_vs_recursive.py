import time


def factorial_iterative(n):
    """
    Computes factorial using an iterative loop.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Computes factorial using recursion.
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative integer (e.g., 20): "))
        if n < 0:
            print("Invalid input! Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Measure Iterative Implementation
    start_iter = time.perf_counter()
    res_iter = factorial_iterative(n)
    end_iter = time.perf_counter()
    iter_time_ns = (end_iter - start_iter) * 1e9

    # Measure Recursive Implementation
    start_rec = time.perf_counter()
    res_rec = factorial_recursive(n)
    end_rec = time.perf_counter()
    rec_time_ns = (end_rec - start_rec) * 1e9

    # Output Results
    print(f"\n--- Results for {n}! ---")
    print(f"Iterative Result : {res_iter}")
    print(f"Iterative Time   : {iter_time_ns:.2f} ns")
    print("-" * 31)
    print(f"Recursive Result : {res_rec}")
    print(f"Recursive Time   : {rec_time_ns:.2f} ns")

    # Time & Space Complexity Summary
    print("\n" + "=" * 60)
    print("           COMPLEXITY ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"{'Method':<22} | {'Time Complexity':<15} | {'Space Complexity':<15}")
    print("-" * 60)
    print(f"{'Iterative Factorial':<22} | {'O(n)':<15} | {'O(1)':<15}")
    print(f"{'Recursive Factorial':<22} | {'O(n)':<15} | {'O(n)':<15}")
    print("=" * 60)


if __name__ == "__main__":
    main()
