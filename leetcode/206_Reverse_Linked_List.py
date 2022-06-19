from typing import Optional
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


class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


class SolutionIterative2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next_node, node.next = node.next, prev
            node, prev = next_node, node
        return prev


class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p


class SolutionRecursive2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None):
            if not node:
                return prev
            next_node, node.next = node.next, prev
            return reverse(next_node, node)

        return reverse(head)


def check_cases(s: Solution):
    assert listnode_to_list(s.reverseList(list_to_listnode([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert listnode_to_list(s.reverseList(list_to_listnode([1, 2]))) == [2, 1]
    assert listnode_to_list(s.reverseList(list_to_listnode([]))) == []


def test_solution():
    check_cases(Solution())


def test_solution_iterative():
    check_cases(SolutionIterative())


def test_solution_iterative2():
    check_cases(SolutionIterative2())


def test_solution_recursive():
    check_cases(SolutionRecursive())


def test_solution_recursive2():
    check_cases(SolutionRecursive2())
