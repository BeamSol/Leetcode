# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return False
        else:
            return False

    return len(stack) == 0
        