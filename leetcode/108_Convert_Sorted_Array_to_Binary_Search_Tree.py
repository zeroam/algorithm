from typing import List
from random import randint

from common.node import TreeNode


class Solution:
    def insertNode(self, node: TreeNode, val: int):
        if node.val is None or val > node.val:
            if node.right:
                self.insertNode(node.right, val)
            else:
                node.right = TreeNode(val)
        elif val < node.val:
            if node.left:
                self.insertNode(node.left, val)
            else:
                node.left = TreeNode(val)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def dfs(node, start: int, end: int):
            mid = (start + end) // 2
            self.insertNode(node, nums[mid])

            if start < mid:
                dfs(node, start, mid - 1)
            if mid < end:
                dfs(node, mid + 1, end)

        dummy_node = TreeNode(None)
        dfs(dummy_node, 0, len(nums) - 1)

        return dummy_node.right


class SolutionLeftMiddleNode:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left: int, right: int):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)


class SolutionRightMiddleNode:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left: int, right: int):
            if left > right:
                return None

            mid = (left + right) // 2
            if (left + right) % 2:
                mid += 1

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)


class SolutionRandomMiddleNode:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left: int, right: int):
            if left > right:
                return None

            mid = (left + right) // 2
            if (left + right) % 2:
                mid += randint(0, 1)

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)
