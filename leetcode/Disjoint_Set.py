from abc import ABC, abstractmethod


class UnionFind(ABC):
    @abstractmethod
    def find(self, x):
        pass

    @abstractmethod
    def union(self, x, y):
        pass

    @abstractmethod
    def connected(self, x, y):
        pass


class QuickFind(UnionFind):
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x
        print(self.root)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class QuickUnion(UnionFind):
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def case1(Solution: UnionFind):
    uf = Solution(10)

    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    assert uf.connected(1, 5) == True
    assert uf.connected(5, 7) == True
    assert uf.connected(4, 9) == False
    uf.union(9, 4)
    assert uf.connected(4, 9) == True


def case2(Solution: UnionFind):
    uf = Solution(10)

    uf.union(1, 2)
    uf.union(5, 6)
    uf.union(5, 7)
    uf.union(2, 5)
    uf.union(3, 8)
    uf.union(3, 9)
    assert uf.connected(1, 5) == True
    assert uf.connected(5, 7) == True


def test_union_find():
    case1(QuickFind)
    case2(QuickFind)


def test_union_find_quick_union():
    case1(QuickUnion)
    case2(QuickUnion)
