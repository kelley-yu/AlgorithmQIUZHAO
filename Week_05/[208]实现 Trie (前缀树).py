class Trie:
    def __init__(self):
        self.trie = {}
        self.end = '#'
    def insert(self, word: str) -> None:
        tree = self.trie
        for i in word:
            tree = tree.setdefault(i, {})
        tree[self.end] = self.end
    def search(self, word: str) -> bool:
        tree = self.trie
        for i in word:
            if i not in tree:
                return False
            tree = tree[i]
        return self.end in tree
    def startsWith(self, prefix: str) -> bool:
        tree = self.trie
        for i in prefix:
            if i not in tree:
                return False
            tree = tree[i]
        return True