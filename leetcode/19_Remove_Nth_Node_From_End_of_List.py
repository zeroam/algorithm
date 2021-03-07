# Definition for singly-linked list.
from typing import List
from common.node import ListNode, listnode_to_list, list_to_listnode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        # count size
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        # find target's prev node and unlink target node
        prev_node = dummy
        for _ in range(size - n):
            prev_node = prev_node.next
        prev_node.next = prev_node.next.next

        return dummy.next


class SolutionTwoPointers:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        # use two pointers
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


def check_solutions(listnode: List[int], n: int, expect: List[int]) -> None:
    s = Solution()
    s_t = SolutionTwoPointers()

    assert listnode_to_list(s.removeNthFromEnd(list_to_listnode(listnode), n)) == expect
    assert listnode_to_list(s_t.removeNthFromEnd(list_to_listnode(listnode), n)) == expect


if __name__ == "__main__":
    listnode = [1]
    n = 1
    expect = []
    check_solutions(listnode, n, expect)

    listnode = [1, 2, 3]
    n = 1
    expect = [1, 2]
    check_solutions(listnode, n, expect)

    listnode = [2, 4, 5]
    n = 3
    expect = [4, 5]
    check_solutions(listnode, n, expect)

    listnode = [2, 4, 5, 6, 7]
    n = 3
    expect = [2, 4, 6, 7]
    check_solutions(listnode, n, expect)