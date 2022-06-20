from typing import Optional
from common.node import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p1, p2 = head, head.next
        while p1 and p2:
            p1.val, p2.val = p2.val, p1.val
            p1 = p1.next.next if p1.next else None
            p2 = p2.next.next if p2.next else None

        return head


def check_cases(s: Solution):
    listnode_to_list(s.swapPairs(list_to_listnode([]))) == []
    listnode_to_list(s.swapPairs(list_to_listnode([1]))) == [1]
    listnode_to_list(s.swapPairs(list_to_listnode([1, 2, 3, 4]))) == [2, 1, 4, 3]
    listnode_to_list(s.swapPairs(list_to_listnode([1, 2, 3, 4, 5]))) == [2, 1, 4, 3, 5]


def test_solution():
    check_cases(Solution())
