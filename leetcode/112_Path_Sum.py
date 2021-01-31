from typing import List
from common.node import TreeNode, make_tree_node


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs_sum(node: TreeNode, total: int) -> bool:
            if node is None:
                return False

            total += node.val
            if node.left is None and node.right is None and total == targetSum:
                return True
            return dfs_sum(node.left, total) or dfs_sum(node.right, total)

        return dfs_sum(root, 0)


class SolutionRecur:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


class SolutionIter:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            cur_node, cur_sum = stack.pop()
            if not cur_node.left and not cur_node.right and cur_sum == 0:
                return True
            if cur_node.right:
                stack.append((cur_node.right, cur_sum - cur_node.right.val))
            if cur_node.left:
                stack.append((cur_node.left, cur_sum - cur_node.left.val))

        return False


def check_solution(l: List[int], target_sum, expect: int) -> None:
    s = Solution()
    s_recur = SolutionRecur()
    s_iter = SolutionIter()

    assert s.hasPathSum(make_tree_node(l), target_sum) == expect
    assert s_recur.hasPathSum(make_tree_node(l), target_sum) == expect
    assert s_iter.hasPathSum(make_tree_node(l), target_sum) == expect


if __name__ == "__main__":
    check_solution([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
    check_solution([1, 2, 3], 5, False)
    check_solution([1, 2], 0, False)
    check_solution([1, 2], 1, False)
