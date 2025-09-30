# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(l):
            if not l:
                return 0
            if l in memo:
                return memo[l]

            rob = dp(l.left) + dp(l.right)
            temp = l.val
            if l.left:
                temp += dp(l.left.left) + dp(l.left.right)
            if l.right:
                temp += dp(l.right.right) + dp(l.right.left)

            memo[l] = max(temp, rob)
            return memo[l]
        return dp(root)