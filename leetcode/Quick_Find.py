class UnionFind:
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


def test_solution():
    uf = UnionFind(10)

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


def test_solution2():
    uf = UnionFind(10)

    uf.union(1, 2)
    uf.union(5, 6)
    uf.union(5, 7)
    uf.union(2, 5)
    uf.union(3, 8)
    uf.union(3, 9)
    assert uf.connected(1, 5) == True
    assert uf.connected(5, 7) == True