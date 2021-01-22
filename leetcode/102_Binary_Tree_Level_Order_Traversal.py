from typing import List
from collections import deque
from common.node import make_tree_node, TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        dq = deque([[root]])
        output = []

        while dq:
            level = dq.popleft()
            next_level = []
            output_item = []
            for curr in level:
                output_item.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)

                if curr.right:
                    next_level.append(curr.right)

            if next_level:
                dq.append(next_level)

            output.append(output_item)

        return output


class SolutionRecursive:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if root is None:
            return levels

        def helper(node: TreeNode, level: int = 0):
            # start the current level
            if level == len(levels):
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root)

        return levels


class SolutionIterative:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if root is None:
            return levels

        level = 0
        dq = deque([root])
        while dq:
            levels.append([])

            level_size = len(dq)
            for _ in range(level_size):
                node = dq.popleft()
                levels[level].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            level += 1

        return levels


def check_solution(case: List[int], expect: List[List[int]]):
    s = Solution()
    s_recursive = SolutionRecursive()
    s_iterative = SolutionIterative()

    assert s.levelOrder(make_tree_node(case)) == expect
    assert s_recursive.levelOrder(make_tree_node(case)) == expect
    assert s_iterative.levelOrder(make_tree_node(case)) == expect


if __name__ == "__main__":
    check_solution([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]])
    check_solution([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
