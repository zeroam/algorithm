import sys
import math
from typing import List
from common.node import TreeNode, make_tree_node


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []

        # inorder traverse
        prev = -sys.maxsize
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node.val <= prev:
                return False

            prev = node.val
            node = node.right

        return True


class SolutionDFS:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(
            node: TreeNode, left: int = -math.inf, right: int = math.inf
        ) -> bool:
            if node is None:
                return True

            if node.val <= left or node.val >= right:
                return False

            return validate(node.left, left, node.val) and validate(
                node.right, node.val, right
            )

        return validate(root)


class SolutionInorder:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = -math.inf

        def inorder(node: TreeNode) -> bool:
            if node is None:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        return inorder(root)


def check_cases(s: Solution):
    s.isValidBST(make_tree_node([2, 1, 3])) is True
    s.isValidBST(make_tree_node([5, 1, 4, None, None, 3, 6])) is False
    s.isValidBST(
        make_tree_node(
            [7, 4, 10, 1, 3, 8, 12, None, None, 2, None, None, 9, None, None]
        )
    ) is False
    s.isValidBST(
        make_tree_node(
            [7, 3, 10, 1, 5, 8, 12, None, None, 4, None, None, 9, None, None]
        )
    ) is True


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_inorder():
    check_cases(SolutionInorder())
