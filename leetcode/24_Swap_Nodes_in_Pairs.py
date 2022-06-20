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


class SolutionSwapVal:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head


class SolutionIterative:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev_node = ListNode(None, head)

        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = prev_node.next

        return root.next


class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


def check_cases(s: Solution):
    listnode_to_list(s.swapPairs(list_to_listnode([]))) == []
    listnode_to_list(s.swapPairs(list_to_listnode([1]))) == [1]
    listnode_to_list(s.swapPairs(list_to_listnode([1, 2, 3, 4]))) == [2, 1, 4, 3]
    listnode_to_list(s.swapPairs(list_to_listnode([1, 2, 3, 4, 5]))) == [2, 1, 4, 3, 5]


def test_solution():
    check_cases(Solution())


def test_solution_swap_val():
    check_cases(SolutionSwapVal())


def test_solution_iterative():
    check_cases(SolutionIterative())


def test_solution_recursive():
    check_cases(SolutionRecursive())
