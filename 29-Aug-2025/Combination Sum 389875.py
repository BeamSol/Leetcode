# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, target, arr, summ_, start):
            if summ_ > target:
                return
            if summ_ == target:
                res.append(arr[:])
                return

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                summ_+=candidates[i]
                backtrack(res, target, arr, summ_, i)
                arr.pop()
                summ_-=candidates[i]
        res=[]
        backtrack(res, target, [],0, 0)
        return res