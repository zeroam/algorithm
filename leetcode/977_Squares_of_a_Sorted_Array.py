from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)


class SolutionPointers:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square * square

        return result


def check_solution(nums: List[int], expect: List[int]):
    s = Solution()
    s_p = SolutionPointers()

    assert s.sortedSquares(nums) == expect
    assert s_p.sortedSquares(nums) == expect


if __name__ == "__main__":
    check_solution([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])
    check_solution([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
