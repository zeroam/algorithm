from collections import deque
from typing import List
from common.node import TreeNode, inorder_traverse


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(l_idx: int, r_idx: int) -> TreeNode:
            if l_idx > r_idx:
                return None

            val = preorder.pop(0)
            node = TreeNode(val)

            idx = idx_map[val]

            node.left = helper(l_idx, idx - 1)
            node.right = helper(idx + 1, r_idx)

            return node

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


class SolutionOrigin:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left = 0, in_right = len(inorder)) -> TreeNode:
            nonlocal pre_idx
            if in_left == in_right:
                return None

            val = preorder[pre_idx]
            node = TreeNode(val)

            pre_idx += 1

            idx = idx_map[val]
            node.left = helper(in_left, idx)
            node.right = helper(idx + 1, in_right)

            return node

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


class SolutionIter:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        dq = deque(preorder)
        root = TreeNode(dq.popleft())
        stack = [root]
        while dq:
            val = dq.popleft()
            node = TreeNode(val)

            # left
            if idx_map[val] < idx_map[stack[-1].val]:
                stack[-1].left = node
            else:
                # right
                while stack and idx_map[stack[-1].val] < idx_map[val]:
                    u = stack.pop()
                u.right = node
            stack.append(node)

        return root


def check_solution(preorder: List[int], inorder: List[int], expect: List[int]) -> None:
    s = Solution()
    s_o = SolutionOrigin()
    s_i = SolutionIter()

    assert inorder_traverse(s.buildTree(preorder.copy(), inorder)) == expect
    assert inorder_traverse(s_o.buildTree(preorder.copy(), inorder)) == expect
    assert inorder_traverse(s_i.buildTree(preorder.copy(), inorder)) == expect


if __name__ == "__main__":
    check_solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [9, 3, 15, 20, 7])
    check_solution([1, 2, 3], [2, 3, 1], [2, 3, 1])
