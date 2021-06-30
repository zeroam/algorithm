class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMinNode(self, root: TreeNode):
        cur = root
        while cur.left is not None:
            cur = cur.left

        return cur

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            if root.right is None:
                temp = root.left
                root = None
                return temp

            min_node = self.findMinNode(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root


class SolutionRecursive:
    def predecessor(self, node: TreeNode) -> int:
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def successor(self, node: TreeNode) -> int:
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

        return root


class SolutionIterative:
    def find_node(self, node: TreeNode, parent: TreeNode, key: int):
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        return node, parent

    def find_min_node(self, node: TreeNode, parent: TreeNode):
        while node.left:
            parent = node
            node = node.left
        return node, parent


    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        dummy = TreeNode(-1)
        dummy.left = root

        node, parent = self.find_node(root, dummy, key)
        if node is None:
            return root

        if node.left is None and node.right is None:
            if parent.right == node:
                parent.right = None
            else:
                parent.left = None
        elif node.left is None:
            if parent.right == node:
                parent.right = node.right
            else:
                parent.left = node.right
        elif node.right is None:
            if parent.right == node:
                parent.right = node.left
            else:
                parent.left = node.left
        else:
            min_node, min_node_parent = self.find_min_node(node.right, node)
            node.val = min_node.val

            # case to node.left is None
            if min_node_parent.right == min_node:
                min_node_parent.right = min_node.right
            else:
                min_node_parent.left = min_node.right

        return dummy.left
