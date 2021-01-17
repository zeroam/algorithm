from typing import List

from common.node import TreeNode, make_tree_node


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
            if root
            else []
        )


class SolutionRecursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode, res: List[int] = []) -> None:
            if root is None:
                return None

            if root.left:
                inorder(root.left, res)
            res.append(root.val)
            if root.right:
                inorder(root.right, res)

        res = []
        inorder(root, res)
        return res


class SolutionStack:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right

        return output


class SolutionMorris:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None

        return res


def check_solution(root: List[int], expect: List[int]):
    s = Solution()
    s_recursive = SolutionRecursive()
    s_stack = SolutionStack()
    s_morris = SolutionMorris()

    assert s.inorderTraversal(make_tree_node(root)) == expect
    assert s_recursive.inorderTraversal(make_tree_node(root)) == expect
    assert s_stack.inorderTraversal(make_tree_node(root)) == expect
    assert s_morris.inorderTraversal(make_tree_node(root)) == expect


if __name__ == "__main__":
    check_solution([1, None, 2, 3], [1, 3, 2])
    check_solution([], [])
    check_solution([1], [1])
    check_solution([1, 2], [2, 1])
    check_solution([1, None, 2], [1, 2])
    check_solution([1, 2, 3, 4, 5, 6, None, None, None, 7, 8], [4, 2, 7, 5, 8, 1, 6, 3])
