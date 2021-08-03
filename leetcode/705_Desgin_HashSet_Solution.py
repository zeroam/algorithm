class MyHashSet:
    def __init__(self):
        self.key_range = 769
        self.bucket = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key: int):
        return key % self.key_range

    def add(self, key: int) -> None:
        bst = self.bucket[self._hash(key)]
        bst.insert(key)

    def remove(self, key: int) -> None:
        bst = self.bucket[self._hash(key)]
        bst.delete(key)

    def contains(self, key: int) -> bool:
        bst = self.bucket[self._hash(key)]
        return bst.search(key)


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BSTree:
    def search(self, node: TreeNode, val: int) -> bool:
        if node is None or val == node.val:
            return node

        if val < node.val:
            return self.search(node.left, val)
        return self.search(node.right, val)

    def insert(self, node: TreeNode, val: int):
        if node is None:
            return TreeNode(val)

        if val > node.val:
            node.right = self.insert(node.right, val)
        if val < node.val:
            node.left = self.insert(node.left, val)

        return node

    def successor(self, node: TreeNode):
        node = node.right
        while node.left:
            node = node.left

        return node.val

    def predecessor(self, node: TreeNode):
        node = node.left
        while node.right:
            node = node.right

        return node.val

    def delete(self, node: TreeNode, val: int):
        if node is None:
            return

        if val < node.val:
            node.left = self.delete(node.left, val)

        if val > node.val:
            node.right = self.delete(node.right, val)

        if val == node.val:
            # the node is a leaf
            if not (node.left or node.right):
                node = None
            elif node.right:
                node.val = self.successor(node)
                node.right = self.delete(node.right, node.val)
            else:
                node.val = self.predecessor(node)
                node.left = self.delete(node.left, node.val)

        return node


class Bucket:
    def __init__(self):
        self.root = None
        self.tree = BSTree()

    def insert(self, value):
        self.root = self.tree.insert(self.root, value)

    def delete(self, value):
        self.root = self.tree.delete(self.root, value)

    def search(self, value):
        return self.tree.search(self.root, value) is not None
