from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        ans = 0
        for a, b in zip(heights, sorted_heights):
            if a != b:
                ans += 1

        return ans


def check_solutions(heights: List[int], expect: int):
    s = Solution()

    assert s.heightChecker(heights) == expect


if __name__ == "__main__":
    check_solutions([1, 2, 3, 4, 5], 0)
    check_solutions([5, 1, 2, 3, 4], 5)
    check_solutions([1, 1, 4, 2, 1, 3], 3)
