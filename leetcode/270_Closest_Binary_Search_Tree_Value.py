from typing import Optional

from common.node import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        left = right = root.val
        if root.left:
            left = self.closestValue(root.left, target)
        if root.right:
            right = self.closestValue(root.right, target)

        return min([left, right, root.val], key=lambda x: abs(x - target))


class SolutionInorder:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(node: TreeNode):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return min(inorder(root), key= lambda x: abs(target - x))


class SolutionIterate:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack, pred = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred <= target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(x - target))

            pred = root.val
            root = root.right

        return pred


class SolutionBinary:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            closest = min(closest, root.val, key=lambda x: abs(x - target))
            root = root.left if target < root.val else root.right
        return closest
