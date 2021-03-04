# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_used = set()

        node_a = headA
        while node_a:
            node_used.add(node_a)
            node_a = node_a.next

        node_b = headB
        while node_b:
            if node_b in node_used:
                return node_b
            node_b = node_b.next

        return None


class SolutionTwoPointers:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a, p_b = headA, headB
        while p_a != p_b:
            p_a = p_a.next if p_a else headB
            p_b = p_b.next if p_b else headA

        return p_a
