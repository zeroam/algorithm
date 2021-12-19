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


class SolutionSimpleBFS:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        output = []
        previous_layer = [root]
        while previous_layer:
            current_layer = []
            level = []

            for node in previous_layer:
                level.append(node.val)
                current_layer.extend(node.children)
            output.append(level)

            previous_layer = current_layer

        return output


class SolutionRecursion:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse_node(node, level):
            if len(output) == level:
                output.append([])

            output[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        if root is None:
            return []

        output = []
        traverse_node(root, 0)
        return output
