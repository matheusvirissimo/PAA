# PAA
Project for the Algorithms Analysis Course, where we analyze the complexity of different sorting algorithms.

Analyzing the complexity of algorithms is crucial for understanding the behavior and efficiency of different sorting methods. It helps predict an algorithm's performance as the size of the data increases. The time and space complexity are the main metrics we evaluate.

# Complexity Order
The complexity order of an algorithm is a way to express its performance behavior in relation to the input size, typically denoted as `n`. This analysis is often divided into three main categories:

1. **Time Complexity**: Refers to the number of operations performed by an algorithm based on the input size. It is described using asymptotic notations, such as `O(n)`, `O(log n)`, `O(n^2)`, etc.
2. **Space Complexity**: Refers to the amount of extra memory an algorithm requires beyond the input size.

# Asymptotic Notations
- **Big O (O)**: Denotes the worst-case scenario of an algorithm, meaning the maximum number of operations it can perform.
- **Big Omega (Ω)**: Represents the best-case scenario, or the minimum number of operations performed.
- **Big Theta (Θ)**: Describes an algorithm's average-case scenario, indicating the exact growth rate in terms of `n`.

# Common Sorting Algorithms

1. **Bubble Sort**:
   - **Time Complexity**: `O(n^2)` in the worst and average cases, `O(n)` in the best case (if the array is already sorted).
   - **Space Complexity**: `O(1)`, as it uses only a constant amount of additional memory.
   - *Explanation*: Bubble Sort makes multiple passes through the list, swapping adjacent elements that are out of order, resulting in quadratic behavior in the worst case.

2. **Merge Sort**:
   - **Time Complexity**: `O(n log n)` in the best, worst, and average cases.
   - **Space Complexity**: `O(n)`, as it uses extra memory to store temporary subarrays during sorting.
   - *Explanation*: It’s a divide-and-conquer algorithm that repeatedly splits the list in half until the subarrays have only one element, then merges them back into a sorted list.

3. **Quick Sort**:
   - **Time Complexity**: `O(n log n)` in the best and average cases, `O(n^2)` in the worst case.
   - **Space Complexity**: `O(log n)` in the best case (recursive implementation), `O(n)` in the worst case.
   - *Explanation*: Quick Sort selects a pivot element and rearranges other elements around it. In the worst case, the chosen pivot is always the largest or smallest, resulting in unbalanced partitions and worse performance.

4. **Heap Sort**:
   - **Time Complexity**: `O(n log n)` in the best, average, and worst cases.
   - **Space Complexity**: `O(1)`, since it is performed in-place.
   - *Explanation*: Heap Sort uses a data structure called a heap to organize the elements. It builds a max heap (or min heap) from the data and repeatedly extracts the largest (or smallest) element to sort them.

# Conclusion
Each sorting algorithm has its advantages and disadvantages depending on the structure of the input data and resource constraints like time and memory. Choosing the ideal algorithm depends on the situation, and complexity analysis is a key tool for understanding and predicting the behavior of algorithms as the data size increases.
