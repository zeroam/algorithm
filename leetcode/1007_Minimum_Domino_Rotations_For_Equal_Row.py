from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        nums = list(set(A + B))
        n = len(A)
        
        count = n
        for num in nums:
            a_rotate, b_rotate = 0, 0
            for a, b in zip(A, B):
                if a == num and b != num:
                    b_rotate += 1
                if b == num and a != num:
                    a_rotate += 1
                if b != num and a != num:
                    break
            else:
                count = min(a_rotate, b_rotate, count)

        return count if count != n else -1


class SolutionOn:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        cnt_a = [0] * 7
        cnt_b = [0] * 7
        cnt_same = [0] * 7

        for a, b in zip(A, B):
            cnt_a[a] += 1
            cnt_b[b] += 1
            if a == b:
                cnt_same[a] += 1

        ans = n
        for v in range(1, 7):
            if cnt_a[v] + cnt_b[v] - cnt_same[v] == n:
                min_swap = min(cnt_a[v], cnt_b[v]) - cnt_same[v]
                ans = min(ans, min_swap)
        return -1 if ans == n else ans


if __name__ == "__main__":
    s = Solution()
    s_on = SolutionOn()

    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    expect = 2
    assert s.minDominoRotations(A, B) == expect
    assert s_on.minDominoRotations(A, B) == expect

    A = [3, 5, 1, 2, 3]
    B = [3, 6, 3, 3, 4]
    expect = -1
    assert s.minDominoRotations(A, B) == expect
    assert s_on.minDominoRotations(A, B) == expect

    A = [1, 1, 1, 1, 1]
    B = [1, 1, 1, 1, 1]
    expect = 0
    assert s.minDominoRotations(A, B) == expect
    assert s_on.minDominoRotations(A, B) == expect

    A = [1, 2, 1, 1, 1, 2, 2, 2]
    B = [2, 1, 2, 2, 2, 2, 2, 2]
    expect = 1
    assert s.minDominoRotations(A, B) == expect
    assert s_on.minDominoRotations(A, B) == expect
