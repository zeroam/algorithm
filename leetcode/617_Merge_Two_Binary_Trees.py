from typing import Optional

from common.node import TreeNode, make_tree_node, compare_tree_node


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if not root1:
            root1 = TreeNode(0)
        if not root2:
            root2 = TreeNode(0)

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


class SolutionRecursive:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2):
            return root1 or root2

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node


def check_case(s: Solution, list1: list[int], list2: list[int], merged_list: list[int]) -> None:
    root1 = make_tree_node(list1)
    root2 = make_tree_node(list2)
    merged = make_tree_node(merged_list)

    compare_tree_node(s.mergeTrees(root1, root2), merged)


def check_cases(s: Solution) -> None:
    check_case(s, [1], [1,2], [2,2])
    check_case(s, [1,3,2,5], [2,1,3,None,4,None,7], [3,4,5,5,4,None,7])


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(SolutionRecursive())
