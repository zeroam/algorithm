import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = 0

        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        node = self.head
        cur_num = 0
        limit = random.randint(0, self.length - 1)

        print(f"length: {self.length}, limit: {limit}")

        while cur_num < limit:
            node = node.next
            cur_num += 1

        return node.val


class SolutionFixedRange:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pick = int(random.random() * len(self.range))
        return self.range[pick]


class SolutionReservoirChosen:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val
            curr = curr.next
            scope += 1

        return chosen_value
