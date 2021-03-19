from typing import List


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        prev = head
        cur = head.next
        min_value = head.val
        max_value = head.val
        while True:
            # check one cycle
            if head is cur:
                break

            if cur.val < min_value:
                min_value = cur.val
            if cur.val > max_value:
                max_value = cur.val

            # over max value
            if prev.val > cur.val and (insertVal < min_value or insertVal > max_value):
                break

            # inserVal is between two values
            if prev.val <= insertVal <= cur.val:
                break

            prev = prev.next
            cur = cur.next

        print(f"prev: {prev.val}, cur: {cur.val}")

        insert_node = Node(insertVal)
        prev.next = insert_node
        insert_node.next = cur

        return head



def check_solution(head: List[int], insert_val: int, expect: List[int]):
    pass

if __name__ == "__main__":
    # case 1: None
    check_solution([], 1, [1])
    # case 2: one
    check_solution([0], 1, [1, 0])
    check_solution([2], 1, [1, 2])

    # case 3: up
    check_solution([3, 4, 1], 2, [3, 4, 1, 2])
    check_solution([3, 4, 1], 5, [3, 4, 5, 2])
    check_solution([1, 4, 6], 3, [1, 3, 4, 6])

    # case 4: down
    check_solution([3, 4, 1], 0, [3, 4, 0, 1])
