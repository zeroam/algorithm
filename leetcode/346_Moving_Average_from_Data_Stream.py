from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) >= self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val

        return self.total / len(self.queue)


class MovingAverageCircularQueue:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0] * size
        self.head = 0
        self.count = 0
        self.total = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.total = self.total - self.queue[tail] + val
        self.head = tail
        self.queue[self.head] = val

        return self.total / min(self.size, self.count)
