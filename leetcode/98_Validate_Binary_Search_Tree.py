import sys
from typing import List
from common.node import TreeNode, make_tree_node


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []

        # inorder traverse
        prev = -sys.maxsize
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node.val <= prev:
                return False

            prev = node.val
            node = node.right

        return True


def check_solutions(node_list: List[int], expect: bool):
    solutions = [Solution()]

    for s in solutions:
        assert s.isValidBST(make_tree_node(node_list)) == expect


if __name__ == "__main__":
    check_solutions([2, 1, 3], True)
    check_solutions([5, 1, 4, None, None, 3, 6], False)
    check_solutions(
        [7, 4, 10, 1, 3, 8, 12, None, None, 2, None, None, 9, None, None], False
    )
    check_solutions(
        [7, 3, 10, 1, 5, 8, 12, None, None, 4, None, None, 9, None, None], True
    )
