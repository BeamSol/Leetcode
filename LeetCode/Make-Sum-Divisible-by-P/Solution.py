1class Solution:
2    def minSubarray(self, nums: List[int], p: int) -> int:
3        prefix = [0]
4        n = len(nums)
5        s = sum(nums) % p
6        if s == 0:
7            return 0
8        for i in range(n):
9            prefix.append((prefix[-1] + nums[i]) % p)
10
11        dic = {0:-1}
12        ans = n
13        for i in range(n+1):
14            if (prefix[i] - s) % p in dic:
15                ans = min(ans, i - dic[(prefix[i] - s) % p])
16            dic[prefix[i]] = i
17        return ans if ans < n else -1