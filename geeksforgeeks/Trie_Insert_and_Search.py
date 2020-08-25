class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        
        
class Trie:
    def __init__(self):
        self.root = self.get_node()
        
    def get_node(self):
        return TrieNode()
        
    def _char_to_index(self, char):
        return ord(char) - ord('a')
        
    def insert(self, key):
        p = self.root

        for c in key:
            index = self._char_to_index(c)
            if p.children[index] is None:
               p.children[index] = self.get_node()
               
            p = p.children[index]
            
        p.is_end_of_word = True
        
    def search(self, key):
        p = self.root

        for c in key:
            index = self._char_to_index(c)
            if p.children[index] is None:
                return False
            p = p.children[index]
            
        return p and p.is_end_of_word


if __name__ == "__main__":
    
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  