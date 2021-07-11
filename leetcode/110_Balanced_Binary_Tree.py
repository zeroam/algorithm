from typing import List, Optional
from common.node import TreeNode, make_tree_node


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        self.ans = True

        def inorder(root: int, h: int):
            if root is None:
                return h

            left_height = inorder(root.left, h + 1)
            right_height = inorder(root.right, h + 1)

            if abs(left_height - right_height) > 1:
                self.ans = False

            return max(left_height, right_height)

        h = inorder(root, 0)

        return self.ans


class SolutionTopDown:
    def height(self, node: TreeNode) -> int:
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return abs(self.height(root.left) - self.height(root.right)) < 2 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)


class SolutionBottomUp:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def balance_check(root: TreeNode):
            if root is None:
                return True, -1

            is_balanced, left_height = balance_check(root.left)
            if not is_balanced:
                return False, 0
            is_balanced, right_height = balance_check(root.right)
            if not is_balanced:
                return False, 0

            return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

        return balance_check(root)[0]


def check_solutions(l: List[Optional[int]], expect: bool):
    solutions = [Solution(), SolutionTopDown(), SolutionBottomUp()]

    for s in solutions:
        assert s.isBalanced(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solutions([], True)
    check_solutions([3, 9, 20, None, None, 15, 7], True)
    check_solutions([1, 2, 2, 3, 3, None, None, 4, 4], False)
    check_solutions([1, 2, 3, 4, 5, 6, None, 8], True)
