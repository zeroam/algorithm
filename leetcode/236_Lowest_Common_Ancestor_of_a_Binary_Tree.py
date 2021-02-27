from common.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        def findTree(cur, p, q):
            if cur is None:
                return False, None

            left, parent_node = findTree(cur.left, p, q)
            if parent_node:
                # 하위노드에서 공통 부모값 리턴 된 경우
                return True, parent_node

            right, parent_node = findTree(cur.right, p, q)
            if parent_node:
                # 하위노드에서 공통 부모값 리턴 된 경우
                return True, parent_node

            if all([left, right]):
                # left, right 하위노드에서 각각 타겟노드를 찾았을 시 현재노드가 공통 부모
                return True, cur
            elif cur in [p, q] and any([left, right]):
                # 현재노드가 타겟노드와 일치 + 하위노드 중 하나가 타겟노드와 일치
                # 현재노드가 공통부모
                return True, cur
            elif cur in [p, q] or left is True or right is True:
                # 현재노드 또는 하위노드가 타겟노드와 일치, 아직 공통부모를 찾지 못했음
                return True, None
            else:
                # 타겟노드를 찾지 못했을 경우
                return False, None

        _, node = findTree(root, p, q)
        return node


class SolutionRecursive:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            # If reached the end of a branch, return False
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


class SolutionIterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers
            if node.left:
                parent[node.left]= node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p
        ancestors = set()

        # Process all ancestors for node p using parent pointers
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q whilch appears in
        # p's ancestor set() is their lowest common ancestor
        while q not in ancestors:
            q = parent[q]
        return q
