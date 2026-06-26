# Big O — Interview Reference

---

## Complexity Classes (fastest → slowest)

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Hash map lookup, array index access |
| O(log n) | Logarithmic | Binary search, balanced BST ops |
| O(n) | Linear | Linear scan, traversal |
| O(n log n) | Linearithmic | Merge sort, heap sort, most fast sorts |
| O(n²) | Quadratic | Nested loops, bubble/insertion/selection sort |
| O(n³) | Cubic | Triple nested loops, naive matrix multiply |
| O(2ⁿ) | Exponential | All subsets, recursive Fibonacci (naive) |
| O(n!) | Factorial | All permutations |

---

## Data Structure Operations

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) | Insert/delete shifts elements |
| Dynamic Array | O(1) | O(n) | O(1) amortized | O(n) | Append is amortized O(1) |
| Linked List | O(n) | O(n) | O(1) | O(1) | Given a pointer to the node |
| Hash Map | — | O(1) avg | O(1) avg | O(1) avg | O(n) worst due to collisions |
| Hash Set | — | O(1) avg | O(1) avg | O(1) avg | Same as hash map |
| Stack | O(n) | O(n) | O(1) | O(1) | Push/pop at top |
| Queue | O(n) | O(n) | O(1) | O(1) | Enqueue/dequeue |
| Binary Heap | O(1) peek | O(n) | O(log n) | O(log n) | Min/max at root |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | AVL, Red-Black |
| BST (unbalanced) | O(n) | O(n) | O(n) | O(n) | Degrades to linked list |
| Trie | — | O(k) | O(k) | O(k) | k = length of key |
| Graph (adj list) | — | O(V+E) | O(1) | O(E) | DFS/BFS is O(V+E) |
| Graph (adj matrix) | O(1) | O(V) | O(1) | O(1) | Space is O(V²) |

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

> Python uses Tim Sort. Java uses Tim Sort for objects, dual-pivot Quick Sort for primitives.

---

## Graph Algorithms

| Algorithm | Time | Space | Notes |
|---|---|---|---|
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| DFS | O(V+E) | O(V) | Stack space is O(h) for trees |
| Dijkstra | O((V+E) log V) | O(V) | No negative edges |
| Bellman-Ford | O(VE) | O(V) | Handles negative edges |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Topological Sort | O(V+E) | O(V) | DAGs only |
| Union-Find | O(α(n)) ≈ O(1) | O(n) | α = inverse Ackermann |
| Prim's MST | O(E log V) | O(V) | Min spanning tree |
| Kruskal's MST | O(E log E) | O(V) | Min spanning tree |

---

## Common Algorithm Patterns & Their Complexities

| Pattern | Time | Space |
|---|---|---|
| Binary search | O(log n) | O(1) |
| Two pointers (sorted) | O(n) | O(1) |
| Sliding window | O(n) | O(1) or O(k) |
| Prefix sum (build) | O(n) | O(n) |
| Prefix sum (query) | O(1) | — |
| BFS/DFS on tree | O(n) | O(h) — h is height |
| BFS/DFS on graph | O(V+E) | O(V) |
| Backtracking (subsets) | O(2ⁿ) | O(n) |
| Backtracking (permutations) | O(n!) | O(n) |
| Top-K with heap | O(n log k) | O(k) |
| Build heap from array | O(n) | O(1) |
| DP (2D) | O(n·m) | O(n·m) or O(n) with rolling array |

---

## Space Complexity Rules

- **Input space** is usually excluded (only extra/auxiliary space counts).
- **Recursion stack** counts — a recursive DFS on a tree of height h uses O(h) space. Worst case (skewed tree) is O(n).
- **Storing output** (e.g. a result list) counts toward space.
- A balanced BST/recursion has O(log n) stack depth; unbalanced is O(n).

---

## How to Analyze Time Complexity

1. **Count loops.** One loop = O(n). Nested loops = multiply: O(n²).
2. **Halving the input each step = O(log n).** (Binary search, tree height)
3. **Doing O(log n) work n times = O(n log n).** (Each heap insert during a build)
4. **Recursion.** Draw the call tree. Total nodes × work per node.
   - Fibonacci (naive): 2 branches, depth n → O(2ⁿ)
   - Merge sort: 2 branches, depth log n, O(n) merge per level → O(n log n)
5. **Drop constants and lower-order terms.** O(2n + 5) → O(n).
6. **Amortized analysis.** Dynamic array append is O(1) amortized because doubling happens rarely.

---

## Recurrence Relations (Master Theorem)

For T(n) = a·T(n/b) + O(nᵈ):

| Condition | Result |
|---|---|
| d > log_b(a) | O(nᵈ) |
| d = log_b(a) | O(nᵈ log n) |
| d < log_b(a) | O(n^(log_b a)) |

**Quick examples:**
- Merge sort: T(n) = 2T(n/2) + O(n) → d=1, log₂2=1 → O(n log n)
- Binary search: T(n) = T(n/2) + O(1) → d=0, log₂1=0 → O(log n)

---

## Interview Tips

- **Always state complexity before coding.** It shows you know the goal.
- **If brute force is O(n²), ask yourself:** can a hash map get this to O(n)? Can sorting + two pointers help?
- **Recursive space = stack depth.** Don't forget it.
- **O(n) space is almost always acceptable** unless the interviewer asks for in-place.
- **"In-place" means O(1) extra space** — the input array itself doesn't count.
- **Amortized O(1)** is still O(1) for interview purposes unless specifically asked.
- When you say O(n), clarify what n is — especially in graphs where V and E are separate.
