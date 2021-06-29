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


class Solution:
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
