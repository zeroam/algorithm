# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def findMax(node: TreeNode, max_ancestor: int, min_ancestor: int) -> int:
            if node is None:
                return 0
            
            diff_from_max = abs(max_ancestor - node.val)
            diff_from_min = abs(min_ancestor - node.val)
            
            max_ancestor = max(node.val, max_ancestor)
            min_ancestor = min(node.val, min_ancestor)
            
            left_max = findMax(node.left, max_ancestor, min_ancestor)
            right_max = findMax(node.right, max_ancestor, min_ancestor)
                
            print(f"node: {node.val}, diff: {diff_from_max}, {diff_from_min}, left_max: {left_max}, right_max: {right_max}")
            
            return max(diff_from_max, diff_from_min, left_max, right_max)
        
        return findMax(root, root.val, root.val)


class SolutionOrigin:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # record the required maximum difference
        self.result = 0
        
        def helper(node: TreeNode, cur_max: int, cur_min: int) -> None:
            if not node:
                return None
            
            # update `result`
            self.result = max(self.result, abs(cur_max - node.val), abs(cur_min - node.val))
            
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result
    