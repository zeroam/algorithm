from collections import deque
from typing import List

from common.node import TreeNode, make_tree_node


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0
        def find_max_depth(node: TreeNode, depth: int = 0) -> None:
            if node is None:
                return

            self.ans = max(self.ans, depth)
            find_max_depth(node.left, depth + 1)
            find_max_depth(node.right, depth + 1)

        find_max_depth(root, 1)

        return self.ans


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        def find_max_depth(node: TreeNode) -> int:
            if node is None:
                return 0

            left_depth = find_max_depth(node.left)
            right_depth = find_max_depth(node.right)
            return max(left_depth, right_depth) + 1

        return find_max_depth(root)


class SolutionBottomUp:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


class SolutionIterative:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(root, 1)]

        depth = 0
        while stack:
            node, cur_depth = stack.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                stack.append((node.left, cur_depth + 1))
                stack.append((node.right, cur_depth + 1))

        return depth


class SolutionBFS:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        dq = deque([root])

        depth = 0
        while dq:
            depth += 1

            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return depth


def check_solution(l: List[int], expect: int):
    s = Solution()
    s2 = Solution2()
    s_bu = SolutionBottomUp()
    s_iterative = SolutionIterative()
    s_bfs = SolutionBFS()

    assert s.maxDepth(make_tree_node(l)) == expect
    assert s2.maxDepth(make_tree_node(l)) == expect
    assert s_bu.maxDepth(make_tree_node(l)) == expect
    assert s_iterative.maxDepth(make_tree_node(l)) == expect
    assert s_bfs.maxDepth(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solution([3, 9, 20, None, None, 15, 7], 3)
    check_solution([1, None, 2], 2)
    check_solution([], 0)
    check_solution([0], 1)
