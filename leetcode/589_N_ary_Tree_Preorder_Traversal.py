from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if len(root.children) == 0:
            return [root.val]

        result = [root.val]
        for node in root.children:
            result += self.preorder(node)

        return result


class SolutionIterative:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output
