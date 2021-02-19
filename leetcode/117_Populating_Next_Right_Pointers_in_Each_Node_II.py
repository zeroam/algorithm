from collections import deque


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


class SolutionPointers:
    def process_child(self, child_node, prev, leftmost):
        if child_node:

            # If the "prev" pointer is already set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = child_node
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = child_node
            prev = child_node
        return prev, leftmost

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we go find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current level.
            curr = leftmost
            prev = None

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established
            while curr:

                # Process both the children and update the prev
                # and leftmost pointers as necessary
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)

                # Move onto the next node.
                curr = curr.next

        return root
