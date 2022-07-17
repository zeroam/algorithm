# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_tree_node(vals: List[int]) -> TreeNode:
    nodes = [None if val == None else TreeNode(val) for val in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def inorder_traverse(root: TreeNode) -> List[int]:
    if root is None:
        return []

    return inorder_traverse(root.left) + [root.val] + inorder_traverse(root.right)


def listnode_to_list(head: ListNode) -> List[int]:
    ret = []
    while head:
        ret.append(head.val)
        head = head.next

    return ret


def list_to_listnode(l: List[int]) -> ListNode:
    dummy = head = ListNode()
    for num in l:
        head.next = ListNode(num)
        head = head.next

    return dummy.next
