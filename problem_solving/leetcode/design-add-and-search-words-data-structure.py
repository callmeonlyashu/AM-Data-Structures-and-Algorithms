"""Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_node = False

    def __repr__(self):
        return f"SELF {list(self.children.keys())}"

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_node = True

    def search(self, word: str) -> bool:
        
        def dfs(root, idx):
            if not root:
                return False

            if idx == len(word):
                return root.end_of_node
            
            if word[idx] != "." and word[idx] not in root.children:
                return False

            if word[idx] == ".":
                for k, v in root.children.items():
                    if dfs(v, idx+1):
                        return True
                return False
            else:
                return dfs(root.children[word[idx]], idx+1)

        return dfs(self.trie, 0)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
