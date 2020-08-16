class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = []
        n, k = len(characters), combinationLength
        
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                self.combs.append("".join(curr))
                return
            
            for i in range(first, n):
                curr.append(characters[i])
                backtrack(i + 1, curr)
                curr.pop()
                
        backtrack()
        self.combs.reverse()
                
    def next(self) -> str:
        return self.combs.pop()
        

    def hasNext(self) -> bool:
        return self.combs
        

if __name__ == "__main__":
    obj = CombinationIterator("abc", 2)
    print(obj.next())
    print(obj.hasNext())
