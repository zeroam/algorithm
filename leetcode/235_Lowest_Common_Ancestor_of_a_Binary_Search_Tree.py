from common.node import TreeNode


class Solution:
    def get_parents(self, root: TreeNode, node: TreeNode):
        parents = []
        while root.val != node.val:
            parents.append(root)
            if node.val < root.val:
                root = root.left
            else:
                root = root.right

        parents.append(node)

        return parents

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_parents = self.get_parents(root, p)
        q_parents = self.get_parents(root, q)

        # compare parents
        size = len(p_parents) if len(p_parents) < len(q_parents) else len(q_parents)

        ans = p_parents[0]
        for i in range(size):
            if p_parents[i] != q_parents[i]:
                break
            ans = p_parents[i]

        return ans
