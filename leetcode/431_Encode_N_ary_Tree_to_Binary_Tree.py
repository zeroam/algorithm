from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if root is None:
            return None

        root_node = TreeNode(root.val)
        queue = deque([(root, root_node)])
        while queue:
            node, new_node = queue.popleft()
            head_node = None
            prev_node = None
            for child in node.children:
                cur_node = TreeNode(child.val)
                if prev_node:
                    prev_node.right = cur_node
                else:
                    head_node = cur_node
                prev_node = cur_node
                queue.append((child, cur_node))

            new_node.left = head_node

        return root_node

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if data is None:
            return None

        root_node = Node(data.val, [])
        queue = deque([(root_node, data)])

        while queue:
            new_node, node = queue.popleft()

            child = node.left
            while child:
                cur_node = Node(child.val, [])
                new_node.children.append(cur_node)
                queue.append((cur_node, child))
                child = child.right
        return root_node


class CodecDFS:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if root is None:
            return None

        root_node = TreeNode(root.val)
        head_node = None
        prev_node = None
        for child in root.children:
            cur_node = self.encode(child)
            if prev_node:
                prev_node.right = cur_node
            else:
                head_node = cur_node
            prev_node = cur_node

        root_node.left = head_node
        return root_node

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if data is None:
            return None

        root_node = Node(data.val, [])

        cur_node = data.left
        while cur_node:
            root_node.children.append(self.decode(cur_node))
            cur_node = cur_node.right

        return root_node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
