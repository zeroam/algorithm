class MinHeap:
    def __init__(self, heap_size: int) -> None:
        self.heap_size = heap_size
        self.heap = [0] * (heap_size + 1)
        self.real_size = 0

    def add(self, element) -> None:
        if self.real_size == self.heap_size:
            print("Added too many element")
            return

        self.real_size += 1
        self.heap[self.real_size] = element

        index = self.real_size
        parent = index // 2
        while (self.heap[index] < self.heap[parent] and index > 1):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def peek(self) -> int:
        return self.heap[1]

    def pop(self) -> int:
        if self.real_size == 0:
            print("Don't have any element!")
            return

        remove_element = self.heap[1]
        self.heap[1] = self.heap[self.real_size]
        self.real_size -= 1

        index = 1
        while (index <= self.real_size // 2):
            left = index * 2
            right = index * 2 + 1
            if (self.heap[index] > self.heap[left] or self.heap[index] > self.heap[right]):
                if self.heap[left] < self.heap[right]:
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                else:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
            else:
                break

        return remove_element

    def size(self) -> int:
        return self.real_size

    def __str__(self) -> str:
        return str(self.heap[1 : self.real_size + 1])


class MaxHeap:
    def __init__(self, heap_size: int) -> None:
        self.heap_size = heap_size
        self.heap = [0] * (heap_size + 1)
        self.real_size = 0

    def add(self, element: int) -> None:
        if self.real_size == self.heap_size:
            print("Added too many element")
            return

        self.real_size += 1
        self.heap[self.real_size] = element

        index = self.real_size
        parent = index // 2
        while (self.heap[index] > self.heap[parent] and index > 1):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def peek(self) -> int:
        return self.heap[1]

    def pop(self) -> int:
        if self.real_size == 0:
            print("Don't have any element!")
            return

        removed_element = self.heap[1]
        self.heap[1] = self.heap[self.real_size]
        self.real_size -= 1

        index = 1
        while index <= self.real_size // 2:
            left = index * 2
            right = index * 2 + 1
            if (self.heap[index] < self.heap[left] or self.heap[index] < self.heap[right]):
                if self.heap[left] > self.heap[right]:
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                else:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
            else:
                break

        return removed_element

    def size(self) -> int:
        return self.real_size

    def __str__(self) -> str:
        return str(self.heap[1 : self.real_size + 1])


def test_min_heap():
    min_heap = MinHeap(5)
    min_heap.add(3)
    min_heap.add(1)
    min_heap.add(2)

    assert str(min_heap) == "[1, 3, 2]"
    assert min_heap.peek() == 1
    assert min_heap.pop() == 1
    assert min_heap.pop() == 2
    assert min_heap.pop() == 3

    min_heap.add(4)
    min_heap.add(5)

    assert str(min_heap) == "[4, 5]"


def test_max_heap():
    max_heap = MaxHeap(5)
    max_heap.add(1)
    max_heap.add(2)
    max_heap.add(3)

    assert str(max_heap) == "[3, 1, 2]"
    assert max_heap.peek() == 3
    assert max_heap.pop() == 3
    assert max_heap.pop() == 2
    assert max_heap.pop() == 1

    max_heap.add(4)
    max_heap.add(5)

    assert str(max_heap) == "[5, 4]"
