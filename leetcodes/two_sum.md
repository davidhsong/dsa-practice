# Two Sum

**Link:** [#1 - Two Sum](https://leetcode.com/problems/two-sum/description/)  
**Difficulty:** Easy
**Date:** 06-27-2026

---

## Pattern

<!-- What pattern does this problem use? (e.g. Sliding Window, Two Pointers, BFS, DP, etc.) -->

- Hash Map
- Enumerate

## Trigger

<!-- What in the problem statement told you to use this pattern? -->

## Key Insight

<!-- The non-obvious observation that unlocks the solution. -->

## Solution

### Using 2 for-loops

```python

```

### Using Hash Map

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in checked.keys():
                return [i, checked.get(comp)]
            checked[v] = i
```

## Complexity

|       |      |
| ----- | ---- |
| Time  | O(n) |
| Space | O(n) |

## Notes

<!-- Edge cases, common mistakes, variations to watch for. -->

- Enumerate: a function in python that creates an enumerate object, which is iterable and is index + value pairs in the form of tuples for every element in the input list/array
- Complement: the complement of each value when iterating through the enumerate object is target minus the current value. If that complement is found in the list of keys from the "checked" hash map, it means the "two sum" indexes have been found and can be returned.
