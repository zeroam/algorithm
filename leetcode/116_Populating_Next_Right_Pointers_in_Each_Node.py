from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return None

        dq = deque([root])
        while dq:
            prev = None
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                if prev:
                    prev.next = node
                prev = node

        return root


class SolutionPointers:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root


class SolutionBFS:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        queue = deque([[root, 1]])
        while queue:
            node, level = queue.popleft()
            if queue and queue[0][1] == level:
                node.next = queue[0][0]

            if node.left and node.right:
                queue.append([node.left, level + 1])
                queue.append([node.right, level + 1])

        return root
