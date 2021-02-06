from typing import List
from common.node import TreeNode, inorder_traverse


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left: int, in_right: int) -> TreeNode:
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtree
            index = idx_map[val]

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)

            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


def check_solution(inorder: List[int], postorder: List[int], expect: List[int]):
    s = Solution()

    assert inorder_traverse(s.buildTree(inorder, postorder)) == expect


if __name__ == "__main__":
    check_solution([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [9, 3, 15, 20, 7])
