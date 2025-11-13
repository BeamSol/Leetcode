class Solution:
    def maxOperations(self, s: str) -> int:
        s_ = ""
        for i in range(len(s)):
            if s[i] == "1":
                s_+= "1"
            elif s_ and s[i] == "0" and s_[-1] == "0":
                continue
            else:
                s_ += "0"
        zero = s_.count("0")
        # print(s_)
        # print(zero)
        temp = 0
        ans = 0
        for i in range(len(s_)):
            if s_[i] == "0":
                ans += (i-temp)
                temp += 1
        return ans
