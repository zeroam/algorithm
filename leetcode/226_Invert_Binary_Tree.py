from collections import deque
from typing import Optional

from common.node import TreeNode, make_tree_node, compare_tree_node


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class SolutionRecursive:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


class SolutionDFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


def check_case(s: Solution, param, expected):
    assert compare_tree_node(
        (s.invertTree(make_tree_node(param))), make_tree_node(expected)
    )


def check_cases(s: Solution):
    check_case(s, [], [])
    check_case(s, [2, 1, 3], [2, 3, 1])
    check_case(s, [4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])


def test_solution():
    check_cases(Solution())


def test_solution_recursive():
    check_cases(SolutionRecursive())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution_dfs():
    check_cases(SolutionDFS())