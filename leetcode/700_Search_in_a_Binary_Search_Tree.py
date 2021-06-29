from common.node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)


class SolutionIteration:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left

        return root
