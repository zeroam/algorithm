from typing import List, Optional

from common.node import TreeNode, make_tree_node


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
            if root
            else []
        )


class SolutionStack:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root], []
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return output[::-1]


class SolutionStack2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push node right -> node -> left
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            else:
                output.append(root.val)
                root = None

        return output


def check_solution(root: List[Optional[int]], output: List[int]):
    s = Solution()
    s_stack = SolutionStack()

    assert s.postorderTraversal(make_tree_node(root)) == output
    assert s_stack.postorderTraversal(make_tree_node(root)) == output


if __name__ == "__main__":
    check_solution([1, None, 2, 3], [3, 2, 1])
    check_solution([], [])
    check_solution([1], [1])
    check_solution([1, 2], [2, 1])
    check_solution([1, None, 2], [2, 1])
    check_solution([1, None, 2, 3, 4, 5], [5, 3, 4, 2, 1])
    check_solution(
        [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, 10, None, 11],
        [8, 4, 5, 2, 9, 10, 6, 11, 7, 3, 1],
    )
