class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            temp = nums[i]%3
            if temp and 3 - temp < temp:
                ans += 3 - temp
            else:
                ans += nums[i]%3
        return ans