# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_occurrences = {}

        for num in nums:
            if num in num_occurrences:
               
                count += num_occurrences[num]
                num_occurrences[num] += 1
            else:
                
                num_occurrences[num] = 1

        return count    