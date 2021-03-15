# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        cur = head
        carry = 0
        while True:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            carry, num = divmod(num1 + num2 + carry, 10)
            cur.next = ListNode(num)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 is None and l2 is None:
                if carry == 0:
                    break

        return head.next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = prev = ListNode(-1)

        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10

            prev.next = ListNode(val)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return prehead.next


def make_list_node(l: list) -> ListNode:
    node = ListNode(val=l[0])
    cur_node = node

    for i in range(1, len(l)):
        cur_node.next = ListNode(l[i])
        cur_node = cur_node.next

    return node


def check_solution(l1: list, l2: list, expect: list):
    solutions = [Solution(), Solution2()]

    for s in solutions:
        node1 = make_list_node(l1)
        node2 = make_list_node(l2)
        expect_node = make_list_node(expect)

        res = s.addTwoNumbers(node1, node2)

        while not None in [expect_node, res]:
            assert expect_node.val == res.val
            expect_node = expect_node.next
            res = res.next

        assert expect_node is None
        assert res is None


if __name__ == "__main__":
    check_solution([2, 4, 3], [5, 6, 4], [7, 0, 8])
    check_solution([0], [0], [0])
    check_solution([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
