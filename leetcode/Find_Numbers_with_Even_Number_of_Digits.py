from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count


def check_solution(nums: List[int], expect: int) -> None:
    s = Solution()

    assert s.findNumbers(nums) == expect


if __name__ == "__main__":
    check_solution([], 0)
    check_solution([12, 345, 2, 6, 7896], 2)
    check_solution([555, 901, 482, 1771], 1)
