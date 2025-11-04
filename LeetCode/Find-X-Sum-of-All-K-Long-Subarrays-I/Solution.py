class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(nums)
        cnt = defaultdict(int)
        l = 0
        heap = []
        for i in range(n):
            cnt[nums[i]]+=1
            heappush(heap, (-cnt[nums[i]], -nums[i]))
            if i - l + 1 == k:
                temp = []
                s = 0
                j = 0
                sets = set()
                while j < x and heap:
                    freq, val = heappop(heap)
                    freq, val = -freq, -val
                    if freq == cnt[val] and val not in sets:
                        temp.append(val)
                        s += freq*val
                        sets.add(val)
                        j += 1
                cnt[nums[l]] -= 1
                l += 1
                ans.append(s)
                for m in range(len(temp)):
                    heappush(heap, (-cnt[temp[m]], -temp[m]))
        return ans

