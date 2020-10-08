# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        length = 1
        cur_node = head
        while cur_node.next is not None:
            length += 1
            cur_node = cur_node.next
        
        new_head = head
        start_node = cur_node
        for _ in range(k % length):
            cur_node = start_node
            cnt = 1
            new_head = ListNode(cur_node.val)
            new_cur_node = new_head
            while cnt != length:
                if cur_node.next is None:
                    cur_node = head
                else:
                    cur_node = cur_node.next
                new_cur_node.next = ListNode(cur_node.val)
                new_cur_node = new_cur_node.next
                cnt += 1
                
            start_node = new_cur_node
            head = new_head

        return new_head


class SolutionBest:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if head is None or head.next is None:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next is not None:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
            
        # find enw tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for _ in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head
        