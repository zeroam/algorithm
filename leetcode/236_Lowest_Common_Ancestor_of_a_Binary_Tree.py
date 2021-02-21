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
