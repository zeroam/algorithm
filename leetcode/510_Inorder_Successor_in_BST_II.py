"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 1. 오른쪽 노드 중 제일 작은 노드
        cur = node.right
        if cur:
            while cur.left:
                cur = cur.left
            return cur

        # 2. 자신이 오른쪽 노드에서 벗어나는 경우
        cur = node
        while cur.parent and cur == cur.parent.right:
            cur = cur.parent
            
        return cur.parent
