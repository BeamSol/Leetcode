# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ''
        for i in s:
            if i.isalnum():
                check += i.lower()
        return check == check[::-1]