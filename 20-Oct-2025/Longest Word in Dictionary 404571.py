# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            ind = ord(w) - ord("a")
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for w in word:
            ind = ord(w) - ord("a")
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]
        return curr.is_end 
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()

        for word in words:
            root.insert(word)
        
        words.sort()
        ans = ""
        for word in words:
            for i in range(1, len(word)):
                if not root.search(word[:i]):
                    break
            else:
                if len(ans) < len(word):
                    ans = word
        return ans

