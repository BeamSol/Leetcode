class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowel = set(("a", "e", "i", "o", "u"))
        ans = 0
        for i in range(n):
            if word[i] in vowel:
                ans += (i + 1) * (n-i)
        return ans