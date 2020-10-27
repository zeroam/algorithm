class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        results = [False] * (n + 1)
        square = 1
        for i in range(1, n + 1):
            if i >= (square + 1) ** 2:
                square += 1
            # print(f"i: {i}", end=" ")
            # print(f"check: (", end=" ")
            for v in range(1, square + 1):
                # print(v, end=", ")
                if results[i - v ** 2] == False:
                    # print(f") value: {v}", end=" ")
                    results[i] = True
                    break
                
            # print(f"result: {results[i]}")
                
        return results[n]


if __name__ == "__main__":
    s = Solution()

    n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expect_list = [True, False, True, True, False, True, False, True, True, False]

    for n, expect in zip(n_list, expect_list):
        assert s.winnerSquareGame(n) == expect

    n = 47
    expect = True
    assert s.winnerSquareGame(n) == expect