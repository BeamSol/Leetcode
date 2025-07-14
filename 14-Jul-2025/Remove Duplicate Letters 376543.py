# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            count[ch]-=1
            if ch in seen:
                continue
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)