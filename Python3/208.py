# Implement Trie

# This trie implementation stores the children letters in an array of lenght 26, 
# where each index is initialized to None.
class TrieNode0:
    # Note that it is not necessary to store the actual character in the node,
    # since it is associated with the index of the array where it is stored in the parent node.
    def __init__(self):
        self.nextLetter = [None]*26 # Store one spot for each letter in alphabet
        self.wordEnd = False # Flag to indicate that this is the last letter of a word that has been stored
        # Note that without this flag, it would be impossible to tell what is just a prefix vs stored word.

class Trie0:

    def __init__(self):
        self.root = TrieNode0()

    def _hash(self, char: str) -> int: # Note that the single underscore shows that this is a private function
        return ord(char) - ord('a') # This function maps the characters a-z to the indices 0-25 in the nextLetter array

    def insert(self, word: str) -> None:
        node = self.root
        for char in word: # Traverse the trie, adding nodes as necessary
            if not node.nextLetter[self.hash(char)]:
                node.nextLetter[self.hash(char)] = TrieNode0()
            node = node.nextLetter[self.hash(char)] # Move to the next node
        
        node.wordEnd = True # Mark the end of the word so it is visible in search

    def search(self, word: str) -> bool:
        node = self.root
        for char in word: # Similar traversal as insert
            if not node.nextLetter[self.hash(char)]:
                return False # If we reach a node that does not exist, the word is not in the trie
            node = node.nextLetter[self.hash(char)]
        
        return node.wordEnd # If the last node is marked as a word end, the word is in the trie

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix: # Same traversal as search
            if not node.nextLetter[self.hash(char)]:
                return False
            node = node.nextLetter[self.hash(char)]
        
        return True # We only care if prefix is tree, so only existence is necessary, not wordEnd.


# This solution differs by using a dictionary instead of an array to store the next letters.
# It seems to run faster on LC, but I think the first solution is a better understanding of a trie.
class TrieNode1:
    def __init__(self):
        self.nextLetter = {}
        self.word_end = False # Note that snake_case is recommended for python variables

class Trie1:

    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.nextLetter:
                node.nextLetter[char] = TrieNode1()
            node = node.nextLetter[char]

        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.nextLetter:
                return False
            node = node.nextLetter[char]
        
        return node.word_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.nextLetter:
                return False
            node = node.nextLetter[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)