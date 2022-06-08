class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        result = 0
        for node in root.children:
            result = max(result, self.maxDepth(node))

        return result + 1


class SolutionIteration:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            cur_depth, root = stack.pop()
            depth = max(depth, cur_depth)
            for node in root.children:
                stack.append((cur_depth + 1, node))

        return depth
