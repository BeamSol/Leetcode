# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sumEven = 0
        for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    sumEven += nums[i]
        for x, y in queries:
            if nums[y] % 2 == 0:
                sumEven -= nums[y]
                nums[y] += x
                if nums[y] % 2 == 0:
                    sumEven += nums[y]
            else:
                nums[y] += x
                if nums[y] % 2 == 0:
                    sumEven += nums[y]
            ans.append(sumEven)
        
        return ans