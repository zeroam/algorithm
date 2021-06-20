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


class Solution2:
    def __init__(self):
        self.previous = None
        self.inorder_successor_node = None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            # case1: has right node
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left

            self.inorder_successor_node = leftmost
        else:
            # case2: don't have right node
            self.inorderCase2(root, p)

        return self.inorder_successor_node

    def inorderCase2(self, node: 'TreeNode', p: 'TreeNode'):
        if node is None:
            return

        self.inorderCase2(node.left, p)

        if self.previous == p and self.inorder_successor_node is None:
            self.inorder_successor_node = node
            return

        self.previous = node

        self.inorderCase2(node.right, p)


class SolutionBST:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        node = root
        while node:
            if node.val <= p.val:
                node = node.right
            else:
                successor = node
                node = node.left

        return successor
