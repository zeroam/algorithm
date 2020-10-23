# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            if node.left:
                q.append((node.left, depth + 1))
                
            if node.right:
                q.append((node.right, depth + 1))
                
            if node.left is None and node.right is None:
                break

        return depth
            


class SolutionSite:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            children = [node.left, node.right]
            if not any(children):
                return depth
            
            for c in children:
                if c:
                    q.append((c, depth + 1))
            