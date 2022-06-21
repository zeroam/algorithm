from typing import Optional

from common.node import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def reverseBetween( self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head

        def reverse(node, prev, count):
            if count == 0:
                return prev

            next_node, node.next = node.next, prev
            return reverse(next_node, node, count - 1)

        dummy = start = ListNode(None, head)
        end = head
        for _ in range(left - 1):
            start = start.next
        for _ in range(right):
            end = end.next

        node = start.next
        p = reverse(node.next, node, right - left)

        start.next = p
        node.next = end
        return dummy.next


def check_cases(s: Solution):
    head = [5]
    left = 1
    right = 1
    expected = [5]
    listnode_to_list(s.reverseBetween(list_to_listnode(head), left, right)) == expected

    head = [1, 2]
    left = 1
    right = 2
    expected = [2, 1]
    listnode_to_list(s.reverseBetween(list_to_listnode(head), left, right)) == expected

    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    expected = [1, 4, 3, 2, 5]
    listnode_to_list(s.reverseBetween(list_to_listnode(head), left, right)) == expected


def test_solution():
    check_cases(Solution())
