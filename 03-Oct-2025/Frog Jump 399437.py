# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] > 1:
            return False

        memo = {}
        def dp(i, k):
            if i == len(stones)-1:
                return True

            if (i,k) in memo:
                return memo[(i,k)]

            ans = False
            if k-1 > 0:
                index = bisect_left(stones, stones[i]+(k-1))
                if 0 <= index < len(stones) and stones[index] == stones[i]+(k-1):
                    ans |= dp(index, k-1)
                
            index = bisect_left(stones, stones[i]+(k))
            if index < len(stones) and stones[index] == stones[i]+(k):
                ans |= dp(index, k)
            
            index = bisect_left(stones, stones[i]+(k+1))
            if index < len(stones) and stones[index] == stones[i]+(k+1):
                ans |= dp(index, k+1)
            
            memo[(i,k)] = ans
            return ans
        return dp(1,1)
            
            
            