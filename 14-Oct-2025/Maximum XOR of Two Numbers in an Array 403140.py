# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None, None]
        root = TrieNode()
        
        for num in nums:
            curr = root
            for i in range(31, -1 , -1):
                indx = (num >> i) & 1
                if not curr.children[indx]:
                    curr.children[indx]  = TrieNode()
                curr = curr.children[indx]
        ans = 0
        for num in nums:
            s = 0
            curr = root
            for i in range(31, -1, -1):
                indx = (num >> i) & 1
                if curr.children[1 - indx ]:
                    s|=(1 << i)
                    curr = curr.children[1-indx]
                else:
                    curr = curr.children[indx]
            ans = max(ans, s)
        return ans
