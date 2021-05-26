from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        cur = None
        while self.q1:
            cur = self.q1.popleft()
            if not self.q1:
                break
            self.q2.append(cur)

        # change q1, q2
        self.q1, self.q2 = self.q2, self.q1

        return cur

    def top(self) -> int:
        """
        Get the top element.
        """
        cur = self.pop()
        if cur:
            self.q1.append(cur)

        return cur

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1


class MyStackSolution1:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # O(n)
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # O(1)
        return self.q1.popleft()

    def top(self) -> int:
        # O(1)
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


class MyStackOneQueue:
    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        # O(n)
        self.q1.append(x)
        size = len(self.q1)
        while size > 1:
            self.q1.append(self.q1.popleft())
            size -= 1

    def pop(self) -> int:
        # O(1)
        return self.q1.popleft()

    def top(self) -> int:
        # O(1)
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
