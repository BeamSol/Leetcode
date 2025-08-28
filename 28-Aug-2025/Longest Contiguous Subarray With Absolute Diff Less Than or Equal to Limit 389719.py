# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minDeque = deque()
        maxDeque = deque()
        lenn = 0
        left = 0
        for i in range(len(nums)):
            while minDeque and minDeque[-1] > nums[i]:
                minDeque.pop()
            minDeque.append(nums[i])
            while maxDeque and maxDeque[-1] < nums[i]:
                maxDeque.pop()
            maxDeque.append(nums[i])

            while maxDeque[0] - minDeque[0] > limit:
                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[left] == minDeque[0]:
                    minDeque.popleft()
                left += 1
            lenn = max(lenn, i-left+1)
        return lenn
