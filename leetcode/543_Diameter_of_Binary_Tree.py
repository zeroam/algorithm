from typing import Optional

from common.node import TreeNode, make_tree_node, inorder_traverse


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal longest
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            longest = max(longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return longest


def check_cases(s: Solution):
    # assert s.diameterOfBinaryTree(make_tree_node([1, 2])) == 1
    # assert s.diameterOfBinaryTree(make_tree_node([1, 2, 3, 4, 5])) == 3
    assert (
        s.diameterOfBinaryTree(
            make_tree_node(
                [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2]
            )
        ) == 8
    )


def test_solution():
    check_cases(Solution())
