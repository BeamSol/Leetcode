class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = [0]
        n = len(nums)
        s = sum(nums) % p
        if s == 0:
            return 0
        for i in range(n):
            prefix.append((prefix[-1] + nums[i]) % p)

        dic = {0:-1}
        ans = n
        for i in range(n+1):
            if (prefix[i] - s) % p in dic:
                ans = min(ans, i - dic[(prefix[i] - s) % p])
            dic[prefix[i]] = i
        return ans if ans < n else -1