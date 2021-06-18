from common.node import TreeNode


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        gt_node = None

        def traverse(node: TreeNode):
            nonlocal gt_node

            if not node:
                return None

            if node.val > p.val and (not gt_node or node.val < gt_node.val):
                gt_node = node

            traverse(node.left)
            #print(node.val)
            traverse(node.right)

        traverse(root)

        return gt_node
