# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(val=None)
        cur = head
        def add_node(l1, l2):
            if l1 is None or l2 is None:
                return 0

            nonlocal cur
            carry = add_node(l1.next, l2.next)
            num = (l1.val + l2.val + carry)
            print(f"carry: {carry}, num: {num}")
            if cur.val is None:
                cur.val = num % 10
            else:
                cur.next = ListNode(num % 10)
                cur = cur.next

            return num // 10

        print(add_node(l1, l2))
        return head


def make_list_node(l: list) -> ListNode:
    node = ListNode(val=l[0])
    cur_node = node

    for i in range(1, len(l)):
        cur_node.next = ListNode(l[i])
        cur_node = cur_node.next

    return node


def check_solution(l1: list, l2: list, expect: list):
    s = Solution()

    l1 = make_list_node(l1)
    l2 = make_list_node(l2)
    expect = make_list_node(expect)

    res = s.addTwoNumbers(l1, l2)

    while not None in [expect, res]:
        assert expect.val == res.val
        expect = expect.next
        res = res.next

    assert expect is None
    assert res is None


if __name__ == "__main__":
    check_solution([2, 4, 3], [5, 6, 4], [7, 0, 8])
    check_solution([0], [0], [0])
    check_solution([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
