import time

INF = 9999


def greedy_change(coins, amount):
    """
    Greedy Method: Picks the largest denomination available first.
    Note: May not always produce the optimal (minimum) number of coins.
    Time Complexity: O(n log n) for sorting + O(amount)
    Space Complexity: O(1)
    """
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    coins_used = []
    rem_amount = amount

    for coin in sorted_coins:
        while rem_amount >= coin:
            coins_used.append(coin)
            rem_amount -= coin
            count += 1

    return count, coins_used


def dp_change(coins, amount):
    """
    Dynamic Programming Method: Bottom-Up Table Construction.
    Always produces the optimal (minimum) number of coins.
    Time Complexity: O(n * amount)
    Space Complexity: O(n * amount)
    """
    n = len(coins)

    # dp[i][j] = minimum coins needed to make amount j using first i coin types
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # Base Cases
    for i in range(n + 1):
        dp[i][0] = 0  # Amount 0 requires 0 coins
    for j in range(1, amount + 1):
        dp[0][j] = INF  # 0 coins available cannot form amount > 0

    # Build DP Table
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i - 1][j]  # Exclude current coin
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)  # Include current coin

    # Print DP Table
    print("\n========== DP TABLE (Min coins for each amount) ==========")
    header = f"{'Coin\\Amt':<10}" + "".join(f"{j:>5}" for j in range(amount + 1))
    print(header)
    print("-" * len(header))

    for i in range(1, n + 1):
        row_str = f"{coins[i - 1]:<10}"
        for j in range(amount + 1):
            val = "-" if dp[i][j] >= INF else str(dp[i][j])
            row_str += f"{val:>5}"
        print(row_str)
    print("-" * len(header))

    return dp[n][amount]


def main():
    # Standard coin denominations from reference
    coins = [1, 5, 6, 9]
    print("Coins available: 1, 5, 6, 9")

    try:
        raw_input = input("Enter target amount (or press Enter to customize coins): ").strip()
        if raw_input:
            amount = int(raw_input)
        else:
            coins_input = input("Enter coin denominations separated by space: ")
            coins = [int(c) for c in coins_input.split()]
            amount = int(input("Enter target amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return

    # Greedy Execution
    start_greedy = time.perf_counter()
    greedy_result, greedy_coins_used = greedy_change(coins, amount)
    end_greedy = time.perf_counter()
    greedy_time_ns = (end_greedy - start_greedy) * 1e9

    # DP Execution
    start_dp = time.perf_counter()
    dp_result = dp_change(coins, amount)
    end_dp = time.perf_counter()
    dp_time_ns = (end_dp - start_dp) * 1e9

    # Output Results
    print("\n" + "=" * 45)
    print("                 RESULTS")
    print("=" * 45)
    print(f"Amount              : {amount}")
    print(f"Greedy Coins Used   : {greedy_coins_used}")
    print(f"Greedy Result       : {greedy_result} coins")
    print(f"Greedy Time         : {greedy_time_ns:.2f} ns")
    print("-" * 45)
    print(f"DP Result           : {dp_result} coins")
    print(f"DP Time             : {dp_time_ns:.2f} ns")
    print("-" * 45)

    # Comparison Summary
    print("\n" + "=" * 45)
    print("               COMPARISON")
    print("=" * 45)
    print(f"{'Method':<12} | {'Coins':<10} | {'Optimal?':<10}")
    print("-" * 45)
    is_greedy_optimal = "Yes" if greedy_result == dp_result else "No"
    print(f"{'Greedy':<12} | {greedy_result:<10} | {is_greedy_optimal:<10}")
    print(f"{'DP':<12} | {dp_result:<10} | {'Yes':<10}")
    print("=" * 45)


if __name__ == "__main__":
    main()
