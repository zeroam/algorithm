class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
            
        node["$"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if ch == ".":
                    for x in node:
                        if x != "$" and search_in_node(word[i + 1:], node[x]):
                            return True
                if ch not in node:
                    return False
                node = node[ch]
                
            return "$" in node
        
        return search_in_node(word, self.trie)
            

if __name__ == "__main__":
    s = WordDictionary()
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    assert s.search("pad") == False
    assert s.search("bad") == True
    assert s.search(".ad") == True
    assert s.search("b..") == True
