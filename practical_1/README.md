# Practical 1: Sorting Algorithms Analysis

This directory contains implementations of five fundamental sorting algorithms in Python. Each script accepts user input to define the array, executes the sorting algorithm, and outputs the sorted array along with its time complexity, space complexity, and precise execution time.

## Algorithms Implemented

1. **Bubble Sort (`bubblesort.py`)**
   - An optimized implementation of Bubble Sort that breaks early if the array is already sorted.
   - **Time Complexity:** Best: $O(n)$, Average: $O(n^2)$, Worst: $O(n^2)$
   - **Space Complexity:** $O(1)$ (In-place)

2. **Insertion Sort (`insertionsort.py`)**
   - A comparison-based sorting algorithm that builds the final sorted array one item at a time.
   - **Time Complexity:** Best: $O(n)$, Average: $O(n^2)$, Worst: $O(n^2)$
   - **Space Complexity:** $O(1)$ (In-place)

3. **Merge Sort (`mergesort.py`)**
   - A divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.
   - **Time Complexity:** Best: $O(n \log n)$, Average: $O(n \log n)$, Worst: $O(n \log n)$
   - **Space Complexity:** $O(n)$ (Auxiliary space for merging)

4. **Quick Sort (`quicksort.py`)**
   - A divide-and-conquer algorithm that selects a 'pivot' element and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
   - **Time Complexity:** Best: $O(n \log n)$, Average: $O(n \log n)$, Worst: $O(n^2)$
   - **Space Complexity:** $O(\log n)$ (Stack space for recursion)

5. **Selection Sort (`selectionsort.py`)**
   - An in-place comparison-based sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist, repeatedly finding the minimum element from the unsorted sublist and moving it to the sorted sublist.
   - **Time Complexity:** Best: $O(n^2)$, Average: $O(n^2)$, Worst: $O(n^2)$
   - **Space Complexity:** $O(1)$ (In-place)

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_1` directory.
3. Run any of the Python files using the Python interpreter:
   ```bash
   python bubblesort.py
   python insertionsort.py
   python mergesort.py
   python quicksort.py
   python selectionsort.py
   ```

### Input Format
The scripts will prompt you to enter the number of elements first, followed by each element one by one:
```text
Enter the number of elements: 5
Enter the elements:
12
3
45
7
8
```

### Output Format
After execution, the program will print:
- The sorted array.
- The theoretical Time and Space complexities.
- The actual execution time in seconds.
