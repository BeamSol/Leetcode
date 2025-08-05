# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

result = []
        for i in range(len(nums)):
            result.append(nums[(i + nums[i]) % len(nums)])
        return result