# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [None for _ in range(26)]

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = self.TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end

            if word[idx] == ".":
                for c in node.children:
                    if c and dfs(c, idx+1):
                        return True
                return False
                
            i = ord(word[idx]) - ord("a")
            if not node.children[i]:
                return False
            return dfs(node.children[i], idx + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)