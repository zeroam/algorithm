from typing import List
from common.node import ListNode, listnode_to_list, list_to_listnode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        size = len(nums)
        for i in range(size // 2):
            if nums[i] != nums[-i - 1]:
                return False

        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        self.ans = True
        self.head = head

        def palindromeCheck(tail: ListNode):
            if tail is None:
                return None

            palindromeCheck(tail.next)

            if self.head.val != tail.val:
                self.ans = False
            self.head = self.head.next

        palindromeCheck(head)

        return self.ans


def check_solution(head: List[int], expect: bool):
    s = Solution()
    s2 = Solution2()

    assert s.isPalindrome(list_to_listnode(head)) == expect
    assert s2.isPalindrome(list_to_listnode(head)) == expect


if __name__ == "__main__":
    check_solution([1], True)
    check_solution([1, 2, 2, 1], True)
    check_solution([1, 2], False)
    check_solution([1, 2, 1], True)
