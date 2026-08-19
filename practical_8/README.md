# Practical 8: Graph Traversal (DFS and BFS) Analysis

This directory contains Python implementations and execution time comparison of two fundamental Graph Traversal algorithms: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.

## Algorithms Implemented

1. **Depth-First Search - DFS (`graph_traversal_dfs_bfs.py`)**
   - Traverses deep into a graph branch before backtracking using recursive call stack.
   - **Time Complexity:** $O(V + E)$ where $V$ is number of vertices and $E$ is number of edges.
   - **Space Complexity:** $O(V)$ for recursion stack and visited array.

2. **Breadth-First Search - BFS (`graph_traversal_dfs_bfs.py`)**
   - Traverses the graph level-by-level using a First-In-First-Out (FIFO) `collections.deque` Queue.
   - **Time Complexity:** $O(V + E)$
   - **Space Complexity:** $O(V)$ for queue and visited array.

---

## Time & Space Complexity Summary

| Method | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **DFS** | $O(V + E)$ | $O(V)$ | Recursion stack depth proportional to graph depth |
| **BFS** | $O(V + E)$ | $O(V)$ | Level-by-level traversal using Queue |

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_8` directory:
   ```bash
   cd practical_8
   ```
3. Run the script using Python:
   ```bash
   python graph_traversal_dfs_bfs.py
   ```

### Example Input / Output

```text
Enter number of vertices: 4
Enter number of edges: 3
Enter edges (u v):
0 1
0 2
1 3
Enter starting vertex: 0

DFS Traversal: 0 1 3 2
BFS Traversal: 0 1 2 3

Execution Time:
DFS: 2500.00 ns
BFS: 3100.00 ns

=======================================================
         GRAPH TRAVERSAL COMPLEXITY SUMMARY
=======================================================
Method     | Time Complexity    | Space Complexity  
-------------------------------------------------------
DFS        | O(V + E)           | O(V)              
BFS        | O(V + E)           | O(V)              
=======================================================
```

## Note on Heap Operations (`.py` artifact cleanup)
Note: If your syllabus also includes Max Heap operations (Build Heap, Insert, Delete Max) under Practical 8, the file [heap_operations.py](file:///c:/Users/badug/Downloads/daa_practicals/practical_8/heap_operations.py) is also available in this folder.
