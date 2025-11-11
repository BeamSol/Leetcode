# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):

            count = 0
            for i in range(len(candies)):
                curr = candies[i]
                count += curr // mid 
                if count >= k:
                    return True
            return False
                
        
        low = 1
        high = sum(candies)//k

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high


        