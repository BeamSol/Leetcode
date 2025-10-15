# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__ (self):
                self.is_end = False
                self.children = [None for _ in range(26)]

        root = TrieNode()
        for dic in dictionary:
            cur = root
            for d in dic:
                idx = ord(d) - ord("a")
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_end = True
        
        def find(word):
            cur = root
            temp = ""
            for w in word:
                idx = ord(w) - ord("a")
                if cur.is_end:
                    return temp
                if not cur.children[idx]:
                    return word
                temp += w
                cur = cur.children[idx]
            return temp
        
        return " ".join([find(word) for word in sentence.split()])


