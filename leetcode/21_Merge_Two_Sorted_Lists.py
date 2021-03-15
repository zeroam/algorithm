from typing import List
from common.node import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        merged = head = ListNode()
        while n1 and n2:
            if n1.val < n2.val:
                merged.next = ListNode(n1.val)
                n1 = n1.next
            else:
                merged.next = ListNode(n2.val)
                n2 = n2.next
            merged = merged.next

        while n1:
            merged.next = ListNode(n1.val)
            merged = merged.next
            n1 = n1.next

        while n2:
            merged.next = ListNode(n2.val)
            merged = merged.next
            n2 = n2.next

        return head.next


class SolutionRecursive:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionIteration:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next


def check_solution(l1: List[int], l2: List[int], expect: List[int]) -> None:
    s = Solution()
    s_r = SolutionRecursive()
    s_i = SolutionIteration()

    assert listnode_to_list(s.mergeTwoLists(list_to_listnode(l1), list_to_listnode(l2))) == expect
    assert listnode_to_list(s_r.mergeTwoLists(list_to_listnode(l1), list_to_listnode(l2))) == expect
    assert listnode_to_list(s_i.mergeTwoLists(list_to_listnode(l1), list_to_listnode(l2))) == expect


if __name__ == "__main__":
    check_solution([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    check_solution([], [], [])
    check_solution([], [0], [0])
