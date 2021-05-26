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

        while self.q2:
            self.q1.append(self.q2.popleft())

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


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
