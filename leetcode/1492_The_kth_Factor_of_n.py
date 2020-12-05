class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 1
        for i in range(1, n + 1):
            if n % i == 0:
                if count == k:
                    return i
                count += 1

        return -1
        

if __name__ == "__main__":
    s = Solution()

    n = 12
    k = 3
    expect = 3
    assert s.kthFactor(n, k) == expect

    n = 7
    k = 2
    expect = 7
    assert s.kthFactor(n, k) == expect

    n = 4
    k = 4
    expect = -1
    assert s.kthFactor(n, k) == expect

    n = 1
    k = 1
    expect = 1
    assert s.kthFactor(n, k) == expect
