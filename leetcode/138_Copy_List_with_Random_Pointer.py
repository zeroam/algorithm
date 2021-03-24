from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        index = 0
        cur = head
        origin_node = []
        new_node = []
        origin_index = {None: -1}
        while cur:
            origin_node.append(cur)
            new_node.append(Node(cur.val))

            origin_index[cur] = index

            cur = cur.next
            index += 1
        new_node.append(None)

        # link
        cur = head
        size = len(origin_node)
        for i in range(size):
            new_node[i].next = new_node[i + 1]
            new_node[i].random = new_node[origin_index[origin_node[i].random]]

        return new_node[0]


class SolutionRecursive:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


class SolutionIterative:
    def __init__(self):
        self.visited = {}

    def getCloneNode(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head not in self.visited:
            self.visited[head] = Node(head.val, None, None)

        return self.visited[head]


    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        old_node = head
        new_node = Node(head.val, None, None)
        self.visited[old_node] = new_node

        while old_node:
            new_node.next = self.getCloneNode(old_node.next)
            new_node.random = self.getCloneNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


def compare_nodes(origin: Node, compare: Node):
    cur_origin = origin
    cur_compare = compare
    while cur_origin or cur_compare:
        origin_val = cur_origin.val if cur_origin else None
        compare_val = cur_compare.val if cur_compare else None
        assert origin_val == compare_val

        origin_random_val = cur_origin.random.val if cur_origin.random else None
        compare_random_val = cur_compare.random.val if cur_compare.random else None
        assert origin_random_val == compare_random_val

        cur_origin = cur_origin.next if cur_origin else None
        cur_compare = cur_compare.next if cur_compare else None


def _make_random_node(l: List[List[Optional[int]]]) -> Node:
    nodes = []
    cur = pre_head = Node(-1)
    for val, _ in l:
        node = Node(val)
        cur.next = node
        cur = cur.next

        nodes.append(Node(val))

    for i, node in enumerate(nodes):
        node.random = l[i][1] if l[i][1] else None

    return pre_head.next


class SolutionIteraviteO1Space:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the originval linked list and the cloned list
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None

            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next

        return head_new


def check_solution(head: list, expect: list):
    s = Solution()
    s_r = SolutionRecursive()
    s_i = SolutionIterative()
    s_i_o1 = SolutionIteraviteO1Space()

    compare_nodes(s.copyRandomList(_make_random_node(head)), _make_random_node(expect))
    compare_nodes(s_r.copyRandomList(_make_random_node(head)), _make_random_node(expect))
    compare_nodes(s_i.copyRandomList(_make_random_node(head)), _make_random_node(expect))
    compare_nodes(s_i_o1.copyRandomList(_make_random_node(head)), _make_random_node(expect))


if __name__ == "__main__":
    target = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    check_solution(target, target)

    target = [[1, 1], [2, 1]]
    check_solution(target, target)

    target = [[3, None], [3, 0], [3, None]]
    check_solution(target, target)

    target = []
    check_solution(target, target)
