# 前缀树 / 字典树
class Trie:
    def __init__(self):
        self.next = {}
        self.is_end = False

    def insert(self, word: str):
        trie = self
        for c in word:
            if c not in trie.next:
                trie.next[c] = Trie()
            trie = trie.next[c]
        trie.is_end = True

    def search(self, word: str) -> bool:
        trie = self
        for c in word:
            if c not in trie.next:
                return False
            trie = trie.next[c]
        return trie.is_end

    def startsWith(self, prefix: str) -> bool:
        trie = self
        for c in prefix:
            if c not in trie.next:
                return False
            trie = trie.next[c]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("abcde")
    t.insert("12345")
    print(t.search("123"))
    print(t.search("12345"))
    print(t.startsWith("abc"))
