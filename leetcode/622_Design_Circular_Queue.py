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


class MyCircularQueueArray:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.count:
            return False

        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.capacity:
            return True
        return False


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueueLinkedList:
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.count:
            return False

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.capacity:
            return True
        return False


class MyCircularQueueList:
    def __init__(self, k: int):
        self.q = [None] * k
        self.limit = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.p2] = value
        self.p2 = (self.p2 + 1) % self.limit
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.p1] = None
        self.p1 = (self.p1 + 1) % self.limit
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.p1]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
