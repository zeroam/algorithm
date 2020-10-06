class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        todo, bit = N, 1
        while todo:
            N ^= bit
            bit = bit << 1
            todo = todo >> 1
        return N
        

if __name__ == "__main__":
    s = Solution()

    N = 5
    expect = 2
    assert s.bitwiseComplement(N) == expect

    N = 7
    expect = 0
    assert s.bitwiseComplement(N) == expect

    N = 10
    expect = 5
    assert s.bitwiseComplement(N) == expect
