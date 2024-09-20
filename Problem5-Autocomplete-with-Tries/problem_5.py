class TrieNode:
    def __init__(self):
        # Initialize an empty dictionary to store children nodes
        self.children = {}
        # Initialize a boolean flag to indicate the end of a word
        self.is_end_of_word = False

    def insert(self, char):
        # Insert a character into the trie
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self, suffix=''):
        # Find all suffixes starting from the current node
        results = []
        if self.is_end_of_word:
            results.append(suffix)
        for char, node in self.children.items():
            results.extend(node.suffixes(suffix + char))
        return results

class Trie:
    def __init__(self):
        # Initialize the root node of the trie
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the trie
        node = self.root
        for char in word:
            node = node.insert(char)
        node.is_end_of_word = True

    def find(self, prefix):
        # Find a prefix in the trie and return the node if found
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

MyTrie = Trie()
wordList = ["ant", "anthology", "antagonist", "antonym", "fun", "function", "factory", "trie", "trigger", "trigonometry", "tripod"]
for word in wordList:
    MyTrie.insert(word)

# Test Case 1: Find suffixes for a prefix that exists
print(MyTrie.find("ant").suffixes())
# Output: ['', 'hology', 'agonist', 'onym']

# Test Case 2: Find suffixes for a prefix that does not exist
print(MyTrie.find("xyz"))
# Output: None

# Test Case 3: Find suffixes for an empty prefix
print(MyTrie.find("").suffixes())
# Output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# Test Case 4: Insert an empty word
MyTrie.insert("")
print(MyTrie.find("").suffixes())
# Output: ['', 'ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# Test Case 5: Insert a very long word
MyTrie.insert("supercalifragilisticexpialidocious")
print(MyTrie.find("supercalifragilisticexpialidocious").is_end_of_word)
# Output: True
