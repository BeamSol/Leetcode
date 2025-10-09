# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = defaultdict(int)

        for num in arr:
            temp = num % k
            if dic[k-temp] == 0:
                dic[temp] += 1
            else:
                dic[k-temp] -= 1
        for key,val in dic.items():
            if val > 0:
                if key == 0 and val % 2 == 0:
                    continue
                return False
        return True