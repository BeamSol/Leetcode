class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        ans = 0
        
        for ch in s:
            if ch == "1":
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
        
        ans += cnt * (cnt + 1) // 2
        return ans % (10**9 + 7)