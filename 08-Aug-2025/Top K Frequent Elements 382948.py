# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr = []
        for key, val in cnt.items():
            arr.append([val,key])
        arr.sort()
        ans=[]
        while len(ans) < k:
            ans.append(arr.pop()[1])
        return ans