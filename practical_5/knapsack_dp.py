import time


def knapsack_dp(weights, values, capacity):
    """
    0/1 Knapsack algorithm using Dynamic Programming.
    Builds a 2D table dp[i][w] representing maximum value achievable
    with first i items and capacity w.
    
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP Table
    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]  # Exclude item i
            if w_i <= w:
                dp[i][w] = max(dp[i][w], v_i + dp[i - 1][w - w_i])  # Include item i

    # Backtrack to identify selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # 0-indexed item index
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], dp, selected_items


def print_dp_table(weights, values, capacity, dp):
    """Prints formatted DP table with aligned headers."""
    n = len(weights)
    print("\n========== 0/1 KNAPSACK DP TABLE ==========")
    header = f"{'Item (w,v)':<15}" + "".join([f"{w:>6}" for w in range(capacity + 1)])
    print(header)
    print("-" * len(header))

    row_0 = f"{'0 (None)':<15}" + "".join([f"{dp[0][w]:>6}" for w in range(capacity + 1)])
    print(row_0)

    for i in range(1, n + 1):
        item_label = f"Item {i} ({weights[i-1]},{values[i-1]})"
        row = f"{item_label:<15}"
        for w in range(capacity + 1):
            row += f"{dp[i][w]:>6}"
        print(row)
    print("-" * len(header))


def main():
    print("0/1 Knapsack Problem using Dynamic Programming")
    print("Press Enter to use default example data, or type inputs.\n")

    try:
        user_input = input("Enter weights (space-separated, e.g., '2 3 4 5') [Default: 2 3 4 5]: ").strip()
        if not user_input:
            weights = [2, 3, 4, 5]
            values = [3, 4, 5, 6]
            capacity = 5
        else:
            weights = list(map(int, user_input.split()))
            values_input = input("Enter values (space-separated, e.g., '3 4 5 6'): ").strip()
            values = list(map(int, values_input.split()))
            capacity = int(input("Enter knapsack capacity: ").strip())

            if len(weights) != len(values):
                print("Error: Weights and values count must match.")
                return
            if capacity < 0:
                print("Error: Capacity must be non-negative.")
                return
    except (ValueError, EOFError):
        print("Using default benchmark data.")
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 5

    print(f"\nItems available: {len(weights)}")
    for idx, (w, v) in enumerate(zip(weights, values), start=1):
        print(f"  Item {idx}: Weight = {w}, Value = {v}")
    print(f"Knapsack Capacity: {capacity}")

    # Solve via DP
    start_time = time.perf_counter()
    max_val, dp_table, items_chosen = knapsack_dp(weights, values, capacity)
    end_time = time.perf_counter()
    exec_time_ns = (end_time - start_time) * 1e9

    # Render DP matrix
    print_dp_table(weights, values, capacity, dp_table)

    # Render output summary
    print("\n========== RESULTS ==========")
    print(f"Maximum Profit Achieved : {max_val}")
    print("Selected Items          : " + ", ".join([f"Item {i+1} (w={weights[i]}, v={values[i]})" for i in items_chosen]))
    print(f"Total Weight Used       : {sum(weights[i] for i in items_chosen)} / {capacity}")
    print(f"Execution Time          : {exec_time_ns:.2f} ns ({exec_time_ns/1e6:.4f} ms)")
    print("=============================")


if __name__ == "__main__":
    main()
