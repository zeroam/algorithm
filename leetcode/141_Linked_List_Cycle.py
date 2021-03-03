# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow_p = head
        fast_p = head
        while fast_p:
            slow_p = slow_p.next
            fast_p = fast_p.next
            if fast_p is None:
                break
            fast_p = fast_p.next

            if slow_p is fast_p:
                return True
        return False


class SolutionHash:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


class SolutionFast:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow_p = head
        fast_p = head.next
        while slow_p != fast_p:
            if fast_p is None or fast_p.next is None:
                return False
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        return True
