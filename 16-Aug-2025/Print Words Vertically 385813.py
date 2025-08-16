# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        max_len = max(len(w) for w in words)
        ans = []
        
        for j in range(max_len):
            strr = ""
            for word in words: 
                if j < len(word):
                    strr += word[j]
                else:
                    strr += " "
            ans.append(strr.rstrip()) 
        return ans
