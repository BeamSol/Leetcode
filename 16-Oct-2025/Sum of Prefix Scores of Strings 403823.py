# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.is_end = False
                self.length = 0
                self.children = [None for _ in range(26)]
        root = TrieNode()
        n = len(words)
        for i in range(n):
            cur = root
            for chr in words[i]:
                idx = ord(chr) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
                cur.length += 1
            cur.is_end = True
        ans = [0] * n
        for i in range(n):
            cur = root
            for chr in words[i]:
                idx = ord(chr) - ord('a')
                ans[i] += cur.length
                cur = cur.children[idx]
            ans[i] += cur.length 

        return ans
