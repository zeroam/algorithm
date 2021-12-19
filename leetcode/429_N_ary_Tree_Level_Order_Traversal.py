from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])

        output = []
        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)

                if node.children is None:
                    continue

                for child in node.children:
                    queue.append(child)

            output.append(nodes)

        return output
