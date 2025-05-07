class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            # If the character is not already a child, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of a word
        node.is_end_of_word = True

    def search(self, word):
        node = self._traverse(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix):
        return self._traverse(prefix) is not None

    def _traverse(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
