""" prefix tree """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search( self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            return node.is_end
        
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("app")
    trie.insert("ban")

    print(trie.search("app"))
    print(trie.search("ban"))
