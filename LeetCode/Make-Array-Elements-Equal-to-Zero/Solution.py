class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        
        # print(prefix)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if prefix[-1]-prefix[i] == prefix[i]:
                    ans += 2
                elif prefix[-1]-prefix[i] == prefix[i] + 1 or prefix[-1]-prefix[i] + 1 == prefix[i]:
                    ans += 1
        return ans