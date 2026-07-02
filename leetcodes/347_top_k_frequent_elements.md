# Problem Name

**Link:** [#347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)  
**Difficulty:** Medium  
**Date:** 07-01-2026

---

## Pattern

<!-- What pattern does this problem use? (e.g. Sliding Window, Two Pointers, BFS, DP, etc.) -->

## Trigger

<!-- What in the problem statement told you to use this pattern? -->

## Key Insight

<!-- The non-obvious observation that unlocks the solution. -->

## Solution

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get, reverse=True)[:k]
```

## Complexity

|       |      |
| ----- | ---- |
| Time  | O(n) |
| Space | O(n) |

## Notes

<!-- Edge cases, common mistakes, variations to watch for. -->
