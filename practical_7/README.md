# Practical 7: Coin Change Problem (Greedy vs Dynamic Programming)

This directory contains Python implementations and a detailed comparative study of solving the **Making Change / Coin Change Problem** using two different design strategies: **Greedy Algorithm** and **Dynamic Programming (DP)**.

## Overview

The Coin Change problem requires finding the minimum number of coins needed to make up a target amount using a given set of coin denominations.

- **Denominations Used:** `[1, 5, 6, 9]`

## Methods Implemented

1. **Greedy Method (`coin_change_greedy_vs_dp.py`)**
   - Always picks the largest coin denomination available that is $\le$ remaining amount.
   - **Time Complexity:** $O(n \log n)$ (due to coin sorting)
   - **Space Complexity:** $O(1)$
   - **Optimality:** Not guaranteed for arbitrary coin systems (e.g. for amount `11` with coins `[1, 5, 6, 9]`, Greedy picks `9 + 1 + 1` = 3 coins, whereas optimal is `6 + 5` = 2 coins).

2. **Dynamic Programming Method (`coin_change_greedy_vs_dp.py`)**
   - Builds a 2D matrix `dp[i][j]` storing the minimum number of coins needed to make amount `j` using the first `i` denominations.
   - **Time Complexity:** $O(n \times \text{amount})$
   - **Space Complexity:** $O(n \times \text{amount})$
   - **Optimality:** Always guarantees the globally optimal solution.

---

## Time & Space Complexity Summary

| Method | Time Complexity | Space Complexity | Optimality | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Greedy** | $O(n \log n)$ | $O(1)$ | No | Fast, but can fail optimal sub-structures |
| **Dynamic Programming** | $O(n \times \text{amount})$ | $O(n \times \text{amount})$ | Yes | Guaranteed minimum coins via full table construction |

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_7` directory:
   ```bash
   cd practical_7
   ```
3. Execute the script using Python:
   ```bash
   python coin_change_greedy_vs_dp.py
   ```

### Example Input / Output

```text
Coins available: [1, 5, 6, 9]
Enter amount: 11

========== DP TABLE (min coins for each amount) ==========
Coin\Amt     0    1    2    3    4    5    6    7    8    9   10   11
---------------------------------------------------------------------
1            0    1    2    3    4    5    6    7    8    9   10   11
5            0    1    2    3    4    1    2    3    4    5    2    3
6            0    1    2    3    4    1    1    2    3    4    2    2
9            0    1    2    3    4    1    1    2    3    1    2    2
---------------------------------------------------------------------

Greedy Coins Used : 9 1 1
DP Coins Used     : 5 6

========== RESULTS ==========
Amount              : 11
Greedy Result       : 3 coins
Greedy Time         : 4200.00 ns
-------------------------------
DP Result           : 2 coins
DP Time             : 15400.00 ns
-------------------------------

========== COMPARISON ==========
Method       | Coins      | Optimal?  
--------------------------------------
Greedy       | 3          | No        
DP           | 2          | Yes       
======================================
```

## Conclusion
While the **Greedy Algorithm** is faster and requires negligible memory, it fails to produce the minimal coin count for non-canonical coin systems. The **Dynamic Programming** approach guarantees optimal solutions by evaluating subproblems systematically.
