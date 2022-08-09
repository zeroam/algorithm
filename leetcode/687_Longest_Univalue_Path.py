from common.node import make_tree_node, TreeNode
from typing import Optional


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: TreeNode, parent: TreeNode = None):
            if node is None:
                return 0

            left = dfs(node.left, node)
            right = dfs(node.right, node)

            if not (node.left and node.left.val == node.val):
                left = 0
            if not (node.right and node.right.val == node.val):
                right = 0

            nonlocal result
            if left + right > result:
                result = left + right

            count = 0
            if parent and parent.val == node.val:
                count += 1
            return count + max(left, right)

        dfs(root)
        return result


class SolutionDFS:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: TreeNode, parent: TreeNode = None):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            nonlocal result
            result = max(result, left + right)

            return max(left, right)

        dfs(root)
        return result


def check_cases(s: Solution):
    assert s.longestUnivaluePath(make_tree_node([5, 4, 5, 1, 1, None, 5])) == 2
    assert s.longestUnivaluePath(make_tree_node([1, 4, 5, 4, 4, None, 5])) == 2
    assert s.longestUnivaluePath(make_tree_node([1, None, 1, 1, 1, 1, 1, 1])) == 4


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())
