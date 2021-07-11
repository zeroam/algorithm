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


def check_solutions(l: List[Optional[int]], expect: bool):
    s = Solution()

    assert s.isBalanced(make_tree_node(l)) == expect


if __name__ == "__main__":
    check_solutions([], True)
    check_solutions([3, 9, 20, None, None, 15, 7], True)
    check_solutions([1, 2, 2, 3, 3, None, None, 4, 4], False)
    check_solutions([1, 2, 3, 4, 5, 6, None, 8], True)
