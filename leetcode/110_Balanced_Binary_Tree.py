from typing import Optional

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


class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


def check_cases(s: Solution):
    assert s.isBalanced(make_tree_node([])) is True
    assert s.isBalanced(make_tree_node([3, 9, 20, None, None, 15, 7])) is True
    assert s.isBalanced(make_tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert s.isBalanced(make_tree_node([1, 2, 3, 4, 5, 6, None, 8])) is True


def test_solution():
    check_cases(Solution())


def test_solution_bottom_up():
    check_cases(SolutionBottomUp())


def test_solution_top_down():
    check_cases(SolutionTopDown())


def test_solution2():
    check_cases(Solution2())
