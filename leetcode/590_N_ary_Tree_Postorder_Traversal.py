from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        for node in root.children:
            result += self.postorder(node)

        result.append(root.val)
        return result


class SolutionIterative:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, result = [root], []
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children)

        return result[::-1]
