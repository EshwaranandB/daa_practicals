# Practical 5: 0/1 Knapsack Problem using Dynamic Programming

This directory contains the Python implementation and detailed analysis of the **0/1 Knapsack Problem** solved using **Dynamic Programming (DP)**.

## Overview

Given $n$ items, each with a weight $w_i$ and a value $v_i$, along with a knapsack capacity $W$, the objective is to select a subset of items to maximize the total value such that the total weight does not exceed $W$. In the 0/1 variation, items cannot be broken into smaller fractions (either take an item completely or leave it).

## Dynamic Programming Formulation

- **State Definition:** Let `dp[i][w]` represent the maximum profit obtainable using a subset of the first `i` items with total capacity `w`.
- **Recurrence Relation:**
  $$dp[i][w] = \begin{cases} dp[i-1][w] & \text{if } w_i > w \\ \max(dp[i-1][w], v_i + dp[i-1][w - w_i]) & \text{if } w_i \le w \end{cases}$$
- **Base Case:** $dp[0][w] = 0$ for all $0 \le w \le W$, and $dp[i][0] = 0$ for all $0 \le i \le n$.

---

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Optimality |
| :--- | :--- | :--- | :--- |
| **0/1 Knapsack (DP)** | $O(n \times W)$ | $O(n \times W)$ | Always Optimal |

> **Note:** The time complexity $O(n \times W)$ is pseudo-polynomial because it depends on the numerical value of the capacity $W$.

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_5` directory:
   ```bash
   cd practical_5
   ```
3. Run the Python script:
   ```bash
   python knapsack_dp.py
   ```

---

## Example Input / Output

```text
0/1 Knapsack Problem using Dynamic Programming
Press Enter to use default example data, or type inputs.

Items available: 4
  Item 1: Weight = 2, Value = 3
  Item 2: Weight = 3, Value = 4
  Item 3: Weight = 4, Value = 5
  Item 4: Weight = 5, Value = 6
Knapsack Capacity: 5

========== 0/1 KNAPSACK DP TABLE ==========
Item (w,v)            0     1     2     3     4     5
------------------------------------------------------
0 (None)              0     0     0     0     0     0
Item 1 (2,3)          0     0     3     3     3     3
Item 2 (3,4)          0     0     3     4     4     7
Item 3 (4,5)          0     0     3     4     5     7
Item 4 (5,6)          0     0     3     4     5     7
------------------------------------------------------

========== RESULTS ==========
Maximum Profit Achieved : 7
Selected Items          : Item 1 (w=2, v=3), Item 2 (w=3, v=4)
Total Weight Used       : 5 / 5
Execution Time          : 12500.00 ns (0.0125 ms)
=============================
```

## Conclusion

The Dynamic Programming strategy ensures global optimality by building upon sub-problems. Backtracking through the `dp` table allows exact identification of which items yield the maximal profit.
