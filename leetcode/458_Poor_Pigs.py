class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        try_cnt = minutesToTest // minutesToDie
        
        pigs = 0
        while (try_cnt + 1) ** pigs < buckets:
            pigs += 1
        
        return pigs


if __name__ == "__main__":
    s = Solution()

    inputs = [4, 15, 15]
    expect = 2
    assert s.poorPigs(*inputs) == expect

    inputs = [4, 15, 30]
    expect = 2
    assert s.poorPigs(*inputs) == expect

    inputs = [8, 15, 15]
    expect = 3
    assert s.poorPigs(*inputs) == expect

    inputs = [8, 15, 30]
    expect = 2
    assert s.poorPigs(*inputs) == expect

    inputs = [1000, 15, 60]
    expect = 5
    assert s.poorPigs(*inputs) == expect
