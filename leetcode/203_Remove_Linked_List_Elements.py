from typing import List
from common.node import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = dummy = ListNode()
        dummy.next = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                continue

            curr = curr.next

        return dummy.next


def check_solution(head: List[int], val: int, expect: List[int]):
    s = Solution()

    assert listnode_to_list(s.removeElements(list_to_listnode(head), val)) == expect


if __name__ == "__main__":
    head = []
    val = 1
    expect = []
    check_solution(head, val, expect)

    head = [7, 7, 7, 7]
    val = 7
    expect = []
    check_solution(head, val, expect)

    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    expect = [1, 2, 3, 4, 5]
    check_solution(head, val, expect)
