from common.node import TreeNode, make_tree_node, compare_tree_node
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

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
