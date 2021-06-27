# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionIter:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        cur_node = root

        if cur_node is None:
            return TreeNode(val)
        
        while cur_node:
            if val < cur_node.val:
                if cur_node.left is None:
                    cur_node.left = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.left
                    
            elif val > cur_node.val:
                if cur_node.right is None:
                    cur_node.right = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.right
                    
        return root
                
        
class SolutionRecur:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root
