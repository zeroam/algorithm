# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        prehead = Node()
        self.flatten = prehead
        def flattenRecursive(node):
            if node is None:
                return None

            child_node = node.child
            next_node = node.next

            self.flatten.next = node
            self.flatten.child = None
            node.prev = self.flatten
            self.flatten = self.flatten.next

            flattenRecursive(child_node)
            flattenRecursive(next_node)

            return node

        flattenRecursive(head)
        prehead.next.prev = None

        return prehead.next


class SolutionDFS:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        prehead = Node()
        def flattenRecursive(prev, curr):
            if curr is None:
                return prev

            curr.prev = prev
            prev.next = curr

            next_node = curr.next
            tail = flattenRecursive(curr, curr.child)
            curr.child = None

            return flattenRecursive(tail, next_node)

        flattenRecursive(prehead, head)
        prehead.next.prev = None

        return prehead.next


class SolutionIteration:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        prev = prehead = Node()
        stack = [head]
        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        prehead.next.prev = None
        return prehead.next
