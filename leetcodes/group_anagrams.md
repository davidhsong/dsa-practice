# Group Anagrams

**Link:** [#49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)  
**Difficulty:** Medium
**Date:** 06-27-2026

---

## Pattern

<!-- What pattern does this problem use? (e.g. Sliding Window, Two Pointers, BFS, DP, etc.) -->

- ## Hash Map

## Trigger

<!-- What in the problem statement told you to use this pattern? -->

## Key Insight

<!-- The non-obvious observation that unlocks the solution. -->

## Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            curWord = "".join(sorted(word))
            if curWord in result.keys():
                result[curWord].append(word)
            else:
                result[curWord] = [word]
        return list(result.values())
```

## Complexity

|       |                 |
| ----- | --------------- |
| Time  | O(n \* k log k) |
| Space | O(n \* k)       |

## Notes

<!-- Edge cases, common mistakes, variations to watch for. -->
