from typing import List, Optional


class ListNode(object):
    def __init__(self, val: int = None):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def _get_node(self, index: int) -> Optional[ListNode]:
        if index < 0 or index >= self.size:
            return None

        cur_index = 0
        cur_node = self.head
        while cur_node and cur_index < index:
            cur_index += 1
            cur_node = cur_node.next

        return cur_node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get_node(index)
        return node.val if node else -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # check add at first
        if index == 0:
            temp_node = self.head
            self.head = ListNode(val)
            self.head.next = temp_node
            self.size += 1
            return

        prev_node = self._get_node(index - 1)
        if prev_node is None:
            return

        cur_node = ListNode(val)
        next_node = prev_node.next

        prev_node.next = cur_node
        cur_node.next = next_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # check delete first node
        if index == 0 and self.head:
            self.head = self.head.next
            self.size -= 1
            return

        prev_node = self._get_node(index - 1)
        if prev_node is None:
            return

        cur_node = prev_node.next
        if cur_node is None:
            return
        next_node = cur_node.next

        prev_node.next = next_node
        self.size -= 1


class MyLinkedListSingly:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # index steps needed
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length,
        # the node will not be inserted
        if index > self.size:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # insert itself
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next


class MyLinkedListDoubly:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def get(self, index: int) -> int:
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        # choose the fatest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val


    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        succ, pred = self.tail, self.tail.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length,
        # the node will not be inserted
        if index > self.size:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        # insertion itself
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred


class MyLinkedListDoubly2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _get_node(self, index: int) -> ListNode:
        if index < 0 or index > self.size:
            return None

        cur_index = 0
        if index < self.size - index:
            # get from head
            cur_node = self.head
            while cur_index < index + 1:
                cur_index += 1
                cur_node = cur_node.next
        else:
            # get from tail
            cur_node = self.tail
            while cur_index < self.size - index:
                cur_index += 1
                cur_node = cur_node.prev

        return cur_node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # validation check
        if index < 0 or index > self.size:
            return None
        cur_node = self._get_node(index)

        prev_node = cur_node.prev
        new_node = ListNode(val)
        new_node.prev = prev_node
        new_node.next = cur_node

        prev_node.next = new_node
        cur_node.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # validation check
        if index < 0 or index >= self.size:
            return None
        cur_node = self._get_node(index)

        prev_node = cur_node.prev
        next_node = cur_node.next

        # cur_node.prev = None
        # cur_node.next = None
        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1


def check_solution(methods: List[str], args_list: List[List[int]], expects: List[Optional[int]]):
    linked_lists = [MyLinkedList(), MyLinkedListSingly(), MyLinkedListDoubly(), MyLinkedListDoubly2()]

    for linked_list in linked_lists:
        for method, args, expect in zip(methods, args_list, expects):
            output = getattr(linked_list, method)(*args)
            assert output == expect


if __name__ == "__main__":
    methods = ["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    args_list = [[1], [3], [1, 2], [1], [1], [1]]
    expects = [None, None, None, 2, None, 3]
    check_solution(methods, args_list, expects)
