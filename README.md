# cs_fundamentals
Instead of framing other frameworks and technologies i have decided to move to core CS topics like DSA and system design, This repo will record my journey of learning them

## The overall strategy

| Track                 | Main goal                                          |
| --------------------- | -------------------------------------------------- |
| **DSA**               | Pass coding rounds                                 |
| **CS Fundamentals**   | Pass technical/theory rounds                       |
| **System/OOP Design** | Handle design questions                            |
| **Practical Systems** | Be able to reason about real backend/cloud systems |


### Month 1 — Complexity + Core DSA
* Big-O
* arrays
* hash tables
* strings
* linked lists
* stacks
* queues

### Month 2 — Algorithms + Trees
* binary search
* sorting
* recursion
* backtracking
* trees
* BST
* heaps
* graph 

### Month 3 — Advanced DSA + OOP
* graph algorithms
* greedy
* DP
* OOP
* composition/inheritance
* SOLID
* design pattern

### Month 4 — OS + continued DSA
* processes
* threads
* scheduling
* synchronization
* deadlocks
* memory
* virtual memory
* filesystems
* Linux

### Month 5 — DBMS + Networking + Linux
* SQL
* indexes
* transactions
* isolation
* DNS
* TCP/IP
* HTTP
* TLS
* Linux
* SSH
* shell

### Month 6 — Interview Mode
This is where everything comes together.
* DSA:
    - mixed problems
    - timed problems
    - mock coding interviews
    - weak-topic revision

* CS:
    - OS questions
    - DBMS questions
    - networking
    - OOP
    - Linux
    - concurrency

* System Design:
    - URL shortener
    - chat
    - file storage
    - feed
    - food delivery backend

* Practical:
    - explain your projects
    - explain architecture
    - explain technical decisions
    - debug scenarios


          ┌──────────────┐
          │    LEARN     │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │  UNDERSTAND  │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │  IMPLEMENT   │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │    SOLVE     │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │   EXPLAIN    │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │     TEST     │
          └──────┬───────┘
                 ↓
          ┌──────────────┐
          │    REVIEW    │
          └──────────────┘
                 │
                 └──→ next concept


#### Give you an unfamiliar LeetCode Medium-style problem.
Understand problem
      ↓
Ask clarifying questions
      ↓
Identify pattern
      ↓
Develop brute force
      ↓
Improve it
      ↓
Write clean code
      ↓
Test edge cases
      ↓
Explain correctness
      ↓
Give time + space complexity

1. Arrays
   ├── Brute Force
   ├── Two Pointers
   ├── Sliding Window
   ├── Prefix Sum
   ├── Hashing
   ├── Binary Search
   └── Kadane

2. Linked Lists
   ├── Fast/Slow Pointers
   ├── Reversal
   ├── Dummy Node
   └── Merge

3. Stack / Queue
   ├── Stack
   ├── Monotonic Stack
   └── BFS

4. Trees
   ├── DFS
   ├── BFS
   ├── BST
   └── Tree recursion

5. Heaps
   ├── Top K
   ├── Kth element
   └── Two Heaps

6. Graphs
   ├── DFS/BFS
   ├── Cycle Detection
   ├── Topological Sort
   ├── Union-Find
   └── Shortest Path

7. Backtracking
   ├── Subsets
   ├── Permutations
   └── Combinations

8. Greedy

9. Dynamic Programming
   ├── 1D
   ├── 2D
   ├── Knapsack
   ├── Subsequence
   └── State-based

10. Advanced
    ├── Trie
    ├── Segment Tree
    ├── Fenwick
    └── Advanced Graph/DP

## Journey
### Month 1 — Complexity + Core DSA
#### Module 1: Time & Space Complexity                                  [29-08-26]
Time complexity = how the number of operations performed by an algorithm grows as the input size n grows.
Space complexity = how much additional memory an algorithm needs as the input size n grows.
	​
Fast
 ↓
O(1)
 ↓
O(log n)
 ↓
O(n)
 ↓
O(n log n)
 ↓
O(n²)
 ↓
O(2ⁿ)
 ↓
O(n!)
Slow

| Complexity   | What is happening?                                  |
| ------------ | --------------------------------------------------- |
| `O(1)`       | Work doesn't grow with `n`                          |
| `O(log n)`   | Problem shrinks/grows exponentially                 |
| `O(n)`       | Process each item once                              |
| `O(n log n)` | `n` work repeated over `log n` levels               |
| `O(n²)`      | Every item interacts with every item                |
| `O(2ⁿ)`      | Each additional input roughly doubles possibilities |
| `O(n!)`      | Number of possible arrangements explodes            |

#### Module 2: Arrays & Strings                                         [30-08-26 -- 04-09-26]  
address(arr[i]) = base_address + i × element_size

When you see a problem that asks you to calculate something about every element, your first thought should often be:
"Can I solve this with one traversal [O(n)] and O(1) extra space?"
eg: Find an element, Find maximum, Find minimum, Count occurrences
##### Methods:
Brute force- O(n²) time, O(1) space
Two pointers- O(n) time, O(1) space
Sliding window-  O(n) time, O(1) space
prefix- O(n)[quering- O(1)] time, O(n) space 


#### Module 2: Sets and Hash maps                                      [05-09-26]  
##### Hash Sets
So a set is particularly useful when our main question is:
"Have I seen this value before?"
rather than:
"Where is this value?"

The hash function helps determine where a value belongs in the underlying hash table.
insert → O(1) average
search → O(1) average
delete → O(1) average

Hash Set = fast membership / existence checking.
--------------------------------------
      Array:                              
            index → value
      Hash Set:
            value → existence
--------------------------------------

##### Hash maps
-------------------------------------------------------
A Set essentially answers:
      Does this value exist?
A Hash Map lets us answer:
      What information is associated with this value?
-------------------------------------------------------
freq[x] = freq.get(x, 0) + 1