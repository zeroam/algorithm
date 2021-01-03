from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findNode(root_node, target_node):
            if root_node is None:
                return None

            if root_node.val == target_node.val:
                return root_node
            ret = findNode(root_node.left, target_node)
            if ret:
                return ret
            ret = findNode(root_node.right, target_node)
            return ret

        return findNode(cloned, target)


class SolutionDFSInorderRecursive:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o is None:
                return None

            inorder(o.left, c.left)
            if o is target:
                self.ans = c
                return
            inorder(o.right, c.right)

        inorder(original, cloned)
        return self.ans


class SolutionDFSInorderIterate:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_o, stack_c = [], []
        node_o, node_c = original, cloned

        while stack_o or node_o:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)

                node_o = node_o.left
                node_c = node_c.left

            node_o = stack_o.pop()
            node_c = stack_c.pop()
            if node_o is target:
                return node_c

            node_o = node_o.right
            node_c = node_c.right



class SolutionBFS:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_o = deque([original,])
        queue_c = deque([cloned,])

        while queue_o:
            node_o = queue_o.popleft()
            node_c = queue_c.popleft()

            if node_o is target:
                return node_c

            if node_o:
                queue_o.append(node_o.left)
                queue_o.append(node_o.right)

                queue_c.append(node_c.left)
                queue_c.append(node_c.right)
