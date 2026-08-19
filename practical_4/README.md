# Practical 4: Factorial Calculation (Iterative vs. Recursive)

This directory contains Python implementations and execution time comparison of calculating factorials using two approaches: **Iterative** and **Recursive**.

## Methods Implemented

1. **Iterative Factorial (`factorial_iterative_vs_recursive.py`)**
   - Uses a simple loop (`for i in range(1, n + 1)`) to accumulate the product.
   - **Time Complexity:** $O(n)$
   - **Space Complexity:** $O(1)$ (In-place scalar allocation)

2. **Recursive Factorial (`factorial_iterative_vs_recursive.py`)**
   - Uses function self-recursion with base condition $n \le 1$.
   - **Time Complexity:** $O(n)$
   - **Space Complexity:** $O(n)$ (Auxiliary stack frames for recursion)

---

## Time & Space Complexity Summary

| Method | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **Iterative Factorial** | $O(n)$ | $O(1)$ | Simple loop, memory efficient |
| **Recursive Factorial** | $O(n)$ | $O(n)$ | Call stack overhead per recursive call |

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_4` directory:
   ```bash
   cd practical_4
   ```
3. Run the script using Python:
   ```bash
   python factorial_iterative_vs_recursive.py
   ```

### Example Input / Output

```text
Enter a non-negative integer (e.g., 20): 10

--- Results for 10! ---
Iterative Result : 3628800
Iterative Time   : 1200.00 ns
-------------------------------
Recursive Result : 3628800
Recursive Time   : 1800.00 ns

============================================================
           COMPLEXITY ANALYSIS SUMMARY
============================================================
Method                 | Time Complexity | Space Complexity
------------------------------------------------------------
Iterative Factorial    | O(n)            | O(1)           
Recursive Factorial    | O(n)            | O(n)           
============================================================
```

## Conclusion
Both iterative and recursive methods perform $n$ multiplications ($O(n)$ time complexity). However, the iterative approach is more space-efficient ($O(1)$ vs $O(n)$ stack space) and avoids stack overflow risks for large values of $n$.
