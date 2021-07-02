from typing import List
from common.node import TreeNode


class BST:
    def __init__(self, nums: List[int]):
        self.size = 0
        self.root = None
        for num in nums:
            self.insert(num)

    def min_value(self):
        node = self.root
        while node.left:
            node = node.left
        return node.val

    def insert(self, num: int):
        self.size += 1

        if self.root is None:
            self.root = TreeNode(num)
            return

        node = self.root
        while node:
            if num < node.val:
                if not node.left:
                    node.left = TreeNode(num)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(num)
                    return
                node = node.right

    def delete(self, num: int, node: TreeNode = None):
        node = node or self.root

        if num < node.val:
            node.left = self.delete(num, node.left)
        elif num > node.val:
            node.right = self.delete(num, node.right)
        else:
            self.size -= 1

            if node.left is None and node.right is None:
                if self.root == node:
                    self.root = None
                return None
            elif node.left is None:
                if self.root == node:
                    self.root = node.right
                return node.right
            elif node.right is None:
                if self.root == node:
                    self.root = node.left
                return node.left
            else:
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left

                node.val = min_node.val
                node.right = self.delete(min_node.val, node.right)

        return node

    def delete_min_node(self):
        min_value = self.min_value()
        self.delete(min_value)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.bst = bst = BST(nums)
        while bst.size > k:
            bst.delete_min_node()

    def add(self, val: int) -> int:
        self.bst.insert(val)
        if self.bst.size > self.k:
            self.bst.delete_min_node()
        return self.bst.min_value()



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)