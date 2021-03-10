from typing import List
from common.node import ListNode, listnode_to_list, list_to_listnode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head


def check_solution(head: List[int], expect: List[int]):
    s = Solution()

    assert listnode_to_list(s.oddEvenList(list_to_listnode(head))) == expect


if __name__ == "__main__":
    head = []
    expect = []
    check_solution(head, expect)

    head = [1]
    expect = [1]
    check_solution(head, expect)

    head = [1, 2]
    expect = [1, 2]
    check_solution(head, expect)

    head = [1, 2, 3]
    expect = [1, 3, 2]
    check_solution(head, expect)

    head = [1, 2, 3, 4, 5, 6]
    expect = [1, 3, 5, 2, 4, 6]
    check_solution(head, expect)
