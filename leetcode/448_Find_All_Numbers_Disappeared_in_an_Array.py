from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = [0] * (n + 1)
        check[0] = 1
        for num in nums:
            check[num] += 1

        ans = []
        for num, cnt in enumerate(check):
            if cnt == 0:
                ans.append(num)

        return ans


class SolutionHashMap:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = set()
        for num in nums:
            check.add(num)

        ans = []
        for num in range(1, n + 1):
            if num not in check:
                ans.append(num)

        return ans


class SolutionO1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            new_index = abs(nums[i]) - 1

            if nums[new_index] > 0:
                nums[new_index] *= -1

        result = []

        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


def check_solution(nums: List[int], expect: List[int]):
    solutions = [Solution(), SolutionHashMap(), SolutionO1()]

    for s in solutions:
        assert s.findDisappearedNumbers(nums) == expect


if __name__ == "__main__":
    check_solution([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])
    check_solution([1, 1], [2])
