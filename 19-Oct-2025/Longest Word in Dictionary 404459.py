# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        check = set(words)
        ans = ""
        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in check:
                    break
            else:
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                
        return ans
