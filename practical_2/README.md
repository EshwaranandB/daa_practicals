# Practical 2: Searching Algorithms Implementation and Time Analysis

This directory contains Python implementations and execution time analysis of two fundamental searching algorithms: **Linear Search** and **Binary Search**. Each script accepts dynamic input from the user, executes the searching algorithm, measures runtime using Python's `time.perf_counter()`, and reports detailed results.

## Algorithms Implemented

1. **Linear Search (`linear_search.py`)**
   - Sequentially checks each element of the list until the target value is found or the list ends.
   - Works on both unsorted and sorted lists.
   - **Time Complexity:** Best: $O(1)$, Average: $O(n)$, Worst: $O(n)$
   - **Space Complexity:** $O(1)$

2. **Binary Search (`binary_search.py`)**
   - Uses a divide-and-conquer strategy by comparing the target to the middle element of a sorted array.
   - Automatically sorts the user-provided array before searching.
   - **Time Complexity:** Best: $O(1)$, Average: $O(\log n)$, Worst: $O(\log n)$
   - **Space Complexity:** $O(1)$

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practicle 2` directory.
3. Execute either script using Python:

```bash
# Run Linear Search
python linear_search.py

# Run Binary Search
python binary_search.py
```

### Example Input / Output

#### Linear Search
```text
Enter numbers separated by spaces (e.g., 5 2 9 1 7): 5 2 9 1 7
Enter the target number to search: 9

--- Results ---
Target 9 found at index: 2
Execution Time: 0.003400 ms
```

#### Binary Search
```text
Enter numbers separated by spaces (e.g., 10 20 30 40 50): 5 2 9 1 7

Sorted List for Binary Search: [1, 2, 5, 7, 9]
Enter the target number to search: 9

--- Results ---
Target 9 found at index: 4 (in sorted array)
Execution Time: 0.002800 ms
```
