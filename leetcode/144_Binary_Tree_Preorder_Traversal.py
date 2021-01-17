from typing import List, Optional

from common.node import TreeNode, make_tree_node


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []

        def preorder(node: TreeNode, ret):
            if node is None:
                return

            ret.append(node.val)
            preorder(node.left, ret)
            preorder(node.right, ret)

        preorder(root, ret)

        return ret


class SolutionStack:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output


class SolutionMorris:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output


def check_solution(root: List[Optional[int]], output: List[int]):
    s = Solution()
    s_stack = SolutionStack()
    s_morris = SolutionMorris()

    assert s.preorderTraversal(make_tree_node(root)) == output
    assert s_stack.preorderTraversal(make_tree_node(root)) == output
    assert s_morris.preorderTraversal(make_tree_node(root)) == output


if __name__ == "__main__":
    check_solution([1, None, 2, 3], [1, 2, 3])
    check_solution([], [])
    check_solution([1], [1])
    check_solution([1, 2], [1, 2])
    check_solution([1, None, 2], [1, 2])
    check_solution([1, None, 2, 3, 4, 5], [1, 2, 3, 5, 4])
