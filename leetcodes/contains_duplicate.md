# Contains Duplicate

**Link:** [#217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)  
**Difficulty:** Easy
**Date:** 06-25-2026

---

## Pattern

<!-- What pattern does this problem use? (e.g. Sliding Window, Two Pointers, BFS, DP, etc.) -->

- Sorting or HashMap

## Trigger

<!-- What in the problem statement told you to use this pattern? -->

-

* checking for duplicates - since sets cannot have duplicates, if I compare the lengths of the original list with that list convert to a set, if there are duplicates, the lengths will not be the same. If the lengths are not the same, then I will know to return True, since different lengths will mean that there is a duplicate.

## Key Insight

<!-- The non-obvious observation that unlocks the solution. -->

## Solution

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return len(nums) != len(temp)

nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
```

## Complexity

|       |     |
| ----- | --- |
| Time  | O() |
| Space | O() |

## Notes

<!-- Edge cases, common mistakes, variations to watch for. -->
