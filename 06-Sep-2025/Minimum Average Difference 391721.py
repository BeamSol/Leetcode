# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        min_diff = float("inf")
        result_index = 0

        for i in range(n):
            left_sum += nums[i]
            left_avg = left_sum // (i + 1)

            if i != n - 1:
                right_sum = total_sum - left_sum
                right_avg = right_sum // (n - i - 1)
            else:
                right_avg = 0

            diff = abs(left_avg - right_avg)

            if diff < min_diff:
                min_diff = diff
                result_index = i

        return result_index
