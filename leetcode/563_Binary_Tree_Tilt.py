# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _sum_node(self, node: TreeNode, total: int = 0) -> int:
        if node is None:
            return 0

        if node.left:
            total = self._sum_node(node.left, total)
        if node.right:
            total = self._sum_node(node.right, total)
            
        return total + node.val

    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        root.val = abs(self._sum_node(root.left) - self._sum_node(root.right))
        
        if root.left:
            self.findTilt(root.left)
            
        if root.right:
            self.findTilt(root.right)
        
        return self._sum_node(root)


def SolutionOrigin:
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def valueSum(node: TreeNode) -> int:
            nonlocal total_tilt

            if node is None:
                return 0

            left_sum = valueSum(node)
            right_sum = valueSum(node)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return left_sum + right_sum + node.val

        valueSum(root)

        return total_tilt
