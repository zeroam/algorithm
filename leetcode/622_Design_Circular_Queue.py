class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.limit = k
        self.queue = [None] * k
        self.circular = False

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head, self.tail = 0, 0
        elif self.tail == self.limit - 1:
            self.tail = 0
            self.circular = True
        else:
            self.tail += 1

        self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head, self.tail = None, None
            self.circular = False
        elif self.head == self.limit - 1:
            self.head = 0
            self.circular = False
        else:
            self.head += 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head is None and self.tail is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == 0 and self.tail == self.limit - 1:
            return True
        if self.circular and self.tail + 1 == self.head:
            return True
        return False
