# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, v):
        cur = self.root
        for w in word:
            idx = ord(w) - ord("a")
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur.val += v
            cur = cur.children[idx]
        cur.val += v
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord("a")
            if not cur.children[idx]:
                return 0
            cur = cur.children[idx]
        return cur.val 
            
class MapSum:
    def __init__(self):
        self.root = Trie()
        self.map = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        v = val - self.map[key]
        self.map[key] = val
        self.root.add(key, v)

    def sum(self, prefix: str) -> int:
        return self.root.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)