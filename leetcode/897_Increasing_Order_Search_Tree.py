# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder_tree(node):
            nonlocal cur_node
            
            if node is None:
                return

            inorder_tree(node.left)
            if cur_node.val == -1:
                cur_node.val = node.val
            else:
                cur_node.right = TreeNode(node.val)
                cur_node = cur_node.right
            print(node.val)
            inorder_tree(node.right)
        
        ordered_node = TreeNode(-1)
        cur_node = ordered_node
        inorder_tree(root)
        
        return ordered_node
        