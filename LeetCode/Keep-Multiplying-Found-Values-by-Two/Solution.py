class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        if ans not in nums:
            return ans

        while ans*2 in nums:
            ans = ans*2
        return ans*2