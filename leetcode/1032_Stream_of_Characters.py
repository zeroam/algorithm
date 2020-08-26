from collections import deque
from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()
        
        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["$"] = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if "$" in node:
                return True
            if ch not in node:
                return False
            
            node = node[ch]
        return "$" in node


if __name__ == "__main__":
    stream_checker = StreamChecker(["cd", "f", "kl"])
    assert stream_checker.query("a") == False
    assert stream_checker.query("b") == False
    assert stream_checker.query("c") == False
    assert stream_checker.query("d") == True
    assert stream_checker.query("e") == False
    assert stream_checker.query("f") == True
    assert stream_checker.query("g") == False
    assert stream_checker.query("h") == False
    assert stream_checker.query("h") == False
    assert stream_checker.query("i") == False
    assert stream_checker.query("j") == False
    assert stream_checker.query("k") == False
    assert stream_checker.query("l") == True
