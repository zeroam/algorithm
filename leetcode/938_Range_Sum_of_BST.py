# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def sumBST(node: TreeNode) -> int:
            if node is None:
                return 0
            
            total = 0
            if low <= node.val <= high:
                total += sumBST(node.left)
                total += sumBST(node.right)
                total += node.val
                    
            elif node.val < low:
                total += sumBST(node.right)
                
            elif node.val > high:
                total += sumBST(node.left)
            
            return total
        
        return sumBST(root)


class SolutionDFS:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode) -> None:
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


class SolutionBFS:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

        return ans
