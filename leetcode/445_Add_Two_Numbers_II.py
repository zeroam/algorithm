# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def make_num(node: ListNode):
        ret = 0
        while node:
            ret *= 10
            ret += node.val
            node = node.next

        return ret
        
    @staticmethod
    def make_node_list(num: int):
        num_str = str(num)
        root = ListNode(int(num_str[0]))
        node = root

        for ch in num_str[1:]:
            node.next = ListNode(int(ch))
            node = node.next

        return root
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        total = Solution.make_num(l1) + Solution.make_num(l2)
        return Solution.make_node_list(total)


def test_case(l1_num: int, l2_num: int, expect: int) -> None:
    l1 = Solution.make_node_list(l1_num)
    l2 = Solution.make_node_list(l2_num)

    assert s.make_num(s.addTwoNumbers(l1, l2)) == expect


if __name__ == "__main__":
    s = Solution()

    test_case(7243, 564, 7807)
    test_case(7243, 5641, 12884)
    test_case(72432, 564, 72996)
