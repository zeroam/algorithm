from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                right = mid + 1
                break
            elif arr[mid] > x:
                right = mid
            else:
                left = mid

        result = []
        for _ in range(k):
            index = self.find_closer(arr, left, right, x)
            result.append(arr[index])
            if index == left:
                left -= 1
            else:
                right += 1

        return sorted(result)

    def find_closer(self, arr: List[int], left: int, right: int, x: int) -> int:
        if left < 0:
            return right
        if right > len(arr) - 1:
            return left

        a, b = arr[left], arr[right]
        a_diff, b_diff = abs(a - x), abs(b - x)

        if a_diff < b_diff:
            return left
        if b_diff < a_diff:
            return right
        if a < b:
            return left
        return right


class SolutionSort:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: abs(num - x))
        return sorted(arr[:k])


class SolutionBinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue

            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return [arr[i] for i in range(left + 1, right)]


def check_cases(s: Solution):
    assert s.findClosestElements([1], 1, 1) == [1]
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert s.findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3) == [-2, -1, 1, 2, 3, 4, 5]
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10]


def test_solution():
    check_cases(Solution())


def test_solution_sort():
    check_cases(SolutionSort())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())
