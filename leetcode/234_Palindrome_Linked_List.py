from typing import Optional
from collections import deque
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


class SolutionList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next

        return l == l[::-1]


class SolutionDeque:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        queue = deque()
        while node:
            queue.append(node.val)
            node = node.next

        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True


class SolutionRunner:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True


def check_cases(s: Solution):
    assert s.isPalindrome(None) == True
    assert s.isPalindrome(list_to_listnode([1])) == True
    assert s.isPalindrome(list_to_listnode([1, 2, 2, 1])) == True
    assert s.isPalindrome(list_to_listnode([1, 2])) == False
    assert s.isPalindrome(list_to_listnode([1, 2, 1])) == True


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())


def test_solution_list():
    check_cases(SolutionList())


def test_solution_deque():
    check_cases(SolutionDeque())


def test_solution_runner():
    check_cases(SolutionRunner())
