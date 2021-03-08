from typing import List
from common.node import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        prev = cur = ListNode(head.val)
        while head.next:
            prev = ListNode(head.next.val)
            prev.next = cur

            cur = prev
            head = head.next

        return prev


def check_solution(l: List[int], expect: List[int]) -> None:
    s = Solution()

    assert listnode_to_list(s.reverseList(list_to_listnode(l))) == expect


if __name__ == "__main__":
    check_solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    check_solution([1, 2], [2, 1])
    check_solution([], [])
