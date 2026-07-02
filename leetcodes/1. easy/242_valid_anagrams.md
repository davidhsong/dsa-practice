# Valid Anagram

**Link:** [#242 - Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)  
**Difficulty:** Easy
**Date:** 06-26-2026

---

## Pattern

<!-- What pattern does this problem use? (e.g. Sliding Window, Two Pointers, BFS, DP, etc.) -->

-

## Trigger

<!-- What in the problem statement told you to use this pattern? -->

## Key Insight

<!-- The non-obvious observation that unlocks the solution. -->

## Solution

### Using Sorting

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
```

### Using Hash Map (counting characters)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
```

## Complexity

|       |      |
| ----- | ---- |
| Time  | O(n) |
| Space | O(n) |

## Notes

<!-- Edge cases, common mistakes, variations to watch for. -->
