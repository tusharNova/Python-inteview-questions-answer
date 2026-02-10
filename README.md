# Python Interview Questions - Logic & Algorithms

## Difficulty: Easy

### 1. Two Sum Problem
Given a list of integers and a target sum, find two numbers that add up to the target.

```python
# Input
nums = [2, 7, 11, 15]
target = 9

# Output
[0, 1]  # indices of 2 and 7

# Constraints
- Return indices of the two numbers
- Each input has exactly one solution
- Cannot use same element twice
```

[Solution](ques/1_twoSum.py)
---

### 2. Reverse a String
Reverse a string without using built-in reverse methods.

```python
# Input
s = "hello"

# Output
"olleh"

# Example
reverse_string("Python") → "nohtyP"
```

---

### 3. Palindrome Check
Check if a string is a palindrome (ignoring spaces, punctuation, and case).

```python
# Input
s = "A man a plan a canal Panama"

# Output
True

# Examples
"racecar" → True
"hello" → False
"12321" → True
"12345" → False
```

---

### 4. FizzBuzz
Print numbers 1 to n, but print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.

```python
# Input
n = 15

# Output
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# Expected Output Type
List or generator
```

---

### 5. Fibonacci Sequence
Generate the first n Fibonacci numbers, or find the nth Fibonacci number efficiently.

```python
# Input 1
n = 7

# Output 1
[1, 1, 2, 3, 5, 8, 13]

# Input 2
find_fibonacci(6)

# Output 2
8  # 6th Fibonacci number

# Constraints
- 0-indexed or 1-indexed?
- Handle negative numbers gracefully
```

---

### 6. Remove Duplicates
Remove duplicates from a list while preserving order.

```python
# Input
nums = [1, 2, 2, 3, 3, 3, 4]

# Output
[1, 2, 3, 4]

# Example
remove_duplicates([5, 1, 2, 1, 3, 2]) → [5, 1, 2, 3]
```

---

### 7. Merge Two Sorted Lists
Merge two sorted lists into one sorted list.

```python
# Input
list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Output
[1, 2, 3, 4, 5, 6]

# Example
merge([1, 5, 9], [2, 3, 8]) → [1, 2, 3, 5, 8, 9]
```

---

### 8. Anagram Check
Check if two strings are anagrams of each other.

```python
# Input
s1 = "listen"
s2 = "silent"

# Output
True

# Examples
is_anagram("evil", "vile") → True
is_anagram("hello", "world") → False
is_anagram("Astronomer", "Moon starer") → True (ignore spaces, case)
```

---

### 9. Find the Missing Number
Given a list containing n distinct numbers from 1 to n+1, find the missing one.

```python
# Input
nums = [3, 0, 1]

# Output
2

# Examples
[0, 1, 3, 4] → 2
[9, 6, 4, 2, 3, 5, 7, 0, 1] → 8
```

---

### 10. Rotate Array
Rotate an array to the right by k steps.

```python
# Input
nums = [1, 2, 3, 4, 5]
k = 2

# Output
[4, 5, 1, 2, 3]

# Examples
[1, 2, 3, 4, 5], k=1 → [5, 1, 2, 3, 4]
[1, 2, 3, 4, 5], k=7 → [4, 5, 1, 2, 3] (k wraps around)
```

---

## Difficulty: Medium

### 11. Find Two Largest Numbers
Find the two largest numbers in a list.

```python
# Input
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Output
[9, 6]

# Examples
find_two_largest([5, 2, 8, 1]) → [8, 5]
find_two_largest([1]) → Error/Exception
find_two_largest([-5, -2, -10]) → [-2, -5]

# Constraints
- List must have at least 2 elements
- Handle duplicates
- What about negative numbers?
- Can you do it in single pass?
```

---

### 12. Find kth Largest Element
Find the kth largest element in an unsorted array.

```python
# Input
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Output
5  # 2nd largest element

# Examples
[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4 → 4
[1, 1, 1, 1], k=2 → 1

# Constraints
- k is always valid
- Optimize for time complexity
```

---

### 13. Longest Substring Without Repeating Characters
Find the length of the longest substring without repeating characters.

```python
# Input
s = "abcabcbb"

# Output
3  # "abc"

# Examples
"bbbbb" → 1  # "b"
"pwwkew" → 3  # "wke"
"au" → 2  # "au"
"dvdf" → 3  # "vdf"
```

---

### 14. Group Anagrams
Group strings that are anagrams of each other.

```python
# Input
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Example
["ab", "ba", "cd", "dc"] → [["ab", "ba"], ["cd", "dc"]]

# Constraints
- Order of groups doesn't matter
- Order within groups doesn't matter
```

---

### 15. Find Duplicate Number
Find the duplicate number in an array of n+1 integers where numbers are between 1 and n.

```python
# Input
nums = [1, 3, 4, 2, 2]

# Output
2

# Examples
[3, 1, 3, 4, 2] → 3
[1, 4, 4, 2, 4] → 4

# Constraints
- Multiple duplicates may exist
- Cannot modify the array
- Cannot use extra space (bonus)
```

---

### 16. Container With Most Water
Given array of heights, find two lines that form a container with most water.

```python
# Input
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Output
49  # (8-1) * 8 = 56 (indices 1 and 8)

# Example
[1, 1] → 1
[4, 3, 2, 1, 4] → 16
```

---

### 17. Valid Parentheses
Check if a string of parentheses is valid (properly matched and ordered).

```python
# Input
s = "({[]})"

# Output
True

# Examples
"()" → True
"([)]" → False  # Incorrect order
"([])" → True
"" → True
"(" → False

# Constraints
- Handle (), [], {}
- Pairs must be properly nested
```

---

### 18. Longest Common Prefix
Find the longest common prefix among a list of strings.

```python
# Input
strings = ["flower", "flow", "flight"]

# Output
"fl"

# Examples
["dog", "racecar", "car"] → ""
["interspecies", "interstellar", "interstate"] → "inters"
["a"] → "a"
```

---

### 19. Majority Element
Find the element that appears more than n/2 times in the array.

```python
# Input
nums = [3, 2, 3]

# Output
3

# Examples
[2, 2, 1, 1, 1, 2, 2] → 2
[1] → 1

# Constraints
- Guaranteed to have a majority element
- Optimize for O(n) time and O(1) space
```

---

### 20. Product of Array Except Self
For each index, return product of all other elements (without using division).

```python
# Input
nums = [1, 2, 3, 4]

# Output
[24, 12, 8, 6]
# nums[0] = 2*3*4 = 24
# nums[1] = 1*3*4 = 12
# nums[2] = 1*2*4 = 8
# nums[3] = 1*2*3 = 6

# Constraints
- Cannot use division operator
- O(n) time complexity
```

---

## Difficulty: Hard

### 21. Find Three Largest Numbers
Find the three largest numbers in a list.

```python
# Input
nums = [10, 5, 8, 12, 3, 6, 20, 15]

# Output
[20, 15, 12]

# Examples
[1, 2, 3, 4, 5] → [5, 4, 3]
[5] → Error/Exception
[-10, -5, -20, -1] → [-1, -5, -10]

# Constraints
- List must have at least 3 elements
- Single pass if possible O(n)
- Handle duplicates and negatives
```

---

### 22. Find kth Smallest Element
Find the kth smallest element in an unsorted array.

```python
# Input
nums = [3, 2, 1, 5, 6, 4]
k = 3

# Output
3

# Examples
[7, 10, 4, 3, 20, 15], k=3 → 7
[1, 1, 1, 1, 1], k=2 → 1

# Constraints
- Optimize for time complexity
- Can you do better than O(n log n)?
```

---

### 23. Word Ladder
Find the shortest transformation sequence from start word to end word.

```python
# Input
start = "hit"
end = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

# Output
5  # hit -> hot -> dot -> dog -> cog

# Constraints
- Only one letter can be changed at a time
- Each transformed word must exist in word_list
- Return length of sequence or -1 if impossible
```

---

### 24. Median of Two Sorted Arrays
Find the median of two sorted arrays.

```python
# Input
nums1 = [1, 3]
nums2 = [2]

# Output
2.0

# Examples
[1, 2], [3, 4] → 2.5
[0, 0], [0, 0] → 0.0

# Constraints
- O(log(min(m, n))) time complexity
- Two arrays of different sizes
```

---

### 25. LRU Cache
Implement an LRU (Least Recently Used) Cache with fixed capacity.

```python
# Operations
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))      # Returns 1
cache.put(3, 3)          # Evicts key 2
print(cache.get(2))      # Returns -1 (not found)
cache.put(4, 4)          # Evicts key 1
print(cache.get(1))      # Returns -1
print(cache.get(3))      # Returns 3
print(cache.get(4))      # Returns 4

# Constraints
- get() and put() must be O(1)
- Capacity is fixed
- Evict least recently used item when full
```

---

### 26. Trapping Rain Water
Calculate how much water can be trapped after raining.

```python
# Input
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# Output
6

# Visualization
#       |
#   |   | |
# | | | | | |
# ---------

# Examples
[4, 2, 0, 3, 2, 5] → 9
[0, 1, 0] → 0

# Constraints
- Use two-pointer approach
- O(n) time, O(1) space
```

---

### 27. Merge K Sorted Lists
Merge k sorted linked lists into one sorted list.

```python
# Input
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

# Output
[1, 1, 2, 3, 4, 4, 5, 6]

# Constraints
- k is the number of linked lists
- Optimize for time complexity
- Use heap/priority queue for efficiency
```

---

### 28. Word Search II
Find all words from a dictionary that exist in a 2D grid.

```python
# Input
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain", "hklf", "hf"]

# Output
["eat", "oath"]

# Constraints
- Each cell is visited once per word search
- Backtracking required
- Use Trie for efficient word lookup
```

---

### 29. Skyline Problem
Given buildings, find the outline of the skyline.

```python
# Input
buildings = [[0,2,3],[2,5,3]]

# Output
[[0, 3], [2, 3], [5, 0]]

# Constraints
- Complex problem
- Use sweep line algorithm
- Handle overlapping buildings
```

---

### 30. Longest Increasing Subsequence
Find the length of the longest increasing subsequence.

```python
# Input
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# Output
4  # [2, 3, 7, 101]

# Examples
[0, 1, 0, 4, 4, 4, 3, 1, 0] → 2
[3, 10, 2, 1, 20] → 3  # [3, 10, 20]

# Constraints
- O(n log n) solution using binary search
- or O(n²) dynamic programming
```

---

## Advanced Concepts

### 31. Implement Trie (Prefix Tree)
Design a data structure for efficient string prefix searches.

```python
trie = Trie()
trie.insert("apple")
trie.search("app")      # False
trie.search("apple")    # True
trie.startsWith("app")  # True
trie.insert("app")
trie.search("app")      # True
```

---

### 32. Implement Union-Find (Disjoint Set)
Design a data structure for efficiently handling connected components.

```python
uf = UnionFind(10)
uf.union(1, 2)
uf.union(3, 4)
uf.find(1) == uf.find(2)  # True
uf.find(1) == uf.find(3)  # False
uf.union(1, 3)
uf.find(1) == uf.find(3)  # True
```

---

### 33. Implement Min Heap
Create a min heap data structure with insert and extract-min operations.

```python
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.extract_min()  # Returns 1
heap.extract_min()  # Returns 3
```

---

### 34. Detect Cycle in Graph
Detect if an undirected/directed graph contains a cycle.

```python
# Undirected Graph
graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
has_cycle(graph)  # True

# Directed Graph
graph = {0: [1], 1: [2], 2: [3], 3: []}
has_cycle_directed(graph)  # False
```

---

### 35. Topological Sort
Sort vertices in a directed acyclic graph (DAG) in topological order.

```python
# Input
edges = [[1, 0], [2, 0], [3, 1], [3, 2]]

# Output
[0, 1, 2, 3]  # One valid topological order

# Use Cases
- Course prerequisites
- Build system dependencies
```

---

## Summary & Tips

1. **Always clarify edge cases** - empty arrays, single elements, negatives, duplicates
2. **Time and space complexity** - Discuss trade-offs
3. **Think out loud** - Walk through your thought process
4. **Test your code** - Use examples during the interview
5. **Optimize iteratively** - Start simple, then optimize
6. **Know your data structures** - lists, sets, dicts, heaps, tries, graphs
7. **Practice patterns** - Two pointers, sliding window, dynamic programming, BFS/DFS
8. **Handle edge cases** - null/empty inputs, single elements, large inputs

---

## Common Interview Patterns

- **Two Pointers**: Palindrome, merge sorted lists, remove duplicates
- **Sliding Window**: Longest substring, minimum window substring
- **Binary Search**: Find target, find boundary, search in rotated array
- **Dynamic Programming**: Fibonacci, LCS, knapsack, coin change
- **Graphs (BFS/DFS)**: Shortest path, connected components, topological sort
- **Hash Maps**: Anagrams, two sum, group elements
- **Heaps**: k-largest, k-smallest, merge k lists
- **Stacks**: Parentheses matching, expression evaluation, monotonic stack
