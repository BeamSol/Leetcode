# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = defaultdict(int)
        set_ = set()
        for num in arr2:
            for n in arr1:
                if num == n:
                    cnt[num]+=1
                    set_.add(num)
        ans= []
        for key,val in cnt.items():
            for i in range(val):
                ans.append(key)
        temp = []
        for n in arr1:
            if n not in set_:
                temp.append(n)
        temp = sorted(temp)
        ans.extend(temp)
        return ans
