1class Solution:
2    def countPartitions(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5        dp = [0] * (n + 1)
6        prefix = [0] * (n + 1)
7        cnt = SortedList()
8
9        dp[0] = 1
10        prefix[0] = 1
11
12        j = 0
13        for i in range(n):
14            cnt.add(nums[i])
15            # adjust window
16            while j <= i and cnt[-1] - cnt[0] > k:
17                cnt.remove(nums[j])
18                j += 1
19            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
20            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
21
22        return dp[n]