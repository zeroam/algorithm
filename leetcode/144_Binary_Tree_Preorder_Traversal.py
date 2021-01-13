from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
