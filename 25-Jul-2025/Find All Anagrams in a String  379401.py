# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt= Counter(p)
        count = Counter()
        res =[]
        k = len(p)

        if len(s) < k:  # Edge case: if s is smaller than p
            return res

        for i in range(k):
            count[s[i]] += 1
        l = 0
        if count == p_cnt:
            res.append(l)
        for r in range(k, len(s)):
            count[s[l]] -= 1
            count[s[r]] += 1
            
            if count[s[l]] == 0:
                del count[s[l]]
            
            l += 1
            if count == p_cnt:
                res.append(l)
        return res
 
            
            

