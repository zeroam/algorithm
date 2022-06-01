from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if len(root.children) == 0:
            return [root.val]

        result = []
        for node in root.children:
            result += self.postorder(node)

        result.append(root.val)
        return result
