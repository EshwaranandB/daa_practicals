# Practical 7: Coin Change Problem (Greedy vs Dynamic Programming)

This directory contains Python implementations and complexity analysis of the **Coin Change Problem** using two different paradigms: **Greedy Approach** and **Dynamic Programming (DP)**.

## Problem Description
Given a set of coin denominations (e.g., `[1, 5, 6, 9]`) and a target amount $N$, find the minimum number of coins needed to make up that amount.

---

## Approaches Implemented

1. **Greedy Approach (`coin_change_greedy_vs_dp.py`)**
   - Always selects the largest coin denomination possible less than or equal to the remaining amount.
   - Fast but **not guaranteed to be optimal** for non-canonical coin systems.
   - **Time Complexity:** $O(n \log n)$ (sorting coins) $+ O(\text{Amount})$
   - **Space Complexity:** $O(1)$

2. **Dynamic Programming Approach (`coin_change_greedy_vs_dp.py`)**
   - Builds a 2D matrix bottom-up where $dp[i][j]$ stores the minimum coins required to form target amount $j$ using first $i$ coin types.
   - **Always optimal**.
   - **Time Complexity:** $O(n \times \text{Amount})$
   - **Space Complexity:** $O(n \times \text{Amount})$

---

## Time & Space Complexity Summary

| Method | Time Complexity | Space Complexity | Optimality | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Greedy** | $O(n \log n)$ | $O(1)$ | May fail (Suboptimal) | Fails on coin sets like `[1, 5, 6, 9]` for amount `11` |
| **Dynamic Programming** | $O(n \times \text{Amount})$ | $O(n \times \text{Amount})$ | **Always Optimal** | Constructs 2D table to explore all subproblems |

---

## How to Run

1. Open terminal and navigate to `practical_7`:
   ```bash
   cd practical_7
   ```
2. Execute the script:
   ```bash
   python coin_change_greedy_vs_dp.py
   ```

### Example Output

```text
Coins available: 1, 5, 6, 9
Enter target amount: 11

Greedy Coins Used : [9, 1, 1]

========== DP TABLE (Min coins for each amount) ==========
Coin\Amt      0    1    2    3    4    5    6    7    8    9   10   11
----------------------------------------------------------------------
1             0    1    2    3    4    5    6    7    8    9   10   11
5             0    1    2    3    4    1    2    3    4    5    2    3
6             0    1    2    3    4    1    1    2    3    4    2    2
9             0    1    2    3    4    1    1    2    3    1    2    2
----------------------------------------------------------------------

=============================================
                 RESULTS
=============================================
Amount              : 11
Greedy Coins Used   : [9, 1, 1]
Greedy Result       : 3 coins
Greedy Time         : 1800.00 ns
---------------------------------------------
DP Result           : 2 coins
DP Time             : 12500.00 ns
---------------------------------------------

=============================================
               COMPARISON
=============================================
Method       | Coins      | Optimal?  
---------------------------------------------
Greedy       | 3          | No        
DP           | 2          | Yes       
=============================================
```
