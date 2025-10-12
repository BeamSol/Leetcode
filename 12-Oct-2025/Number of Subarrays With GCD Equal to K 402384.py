# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        temp = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = gcd(temp, nums[j])
                if temp == k:
                    ans += 1
                elif temp < k:
                    break
                
        return ans