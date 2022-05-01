from bisect import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if mid + 1 == len(letters):
                    return letters[0]
                if letters[mid + 1] > target:
                    return letters[mid + 1]
                else:
                    left = mid + 1
            elif letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left % len(letters)]


class SolutionSeen:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord("a") + i) % 26 + ord("a"))
            if cand in seen:
                return cand


class SolutionLinear:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return letters[0]


class SolutionBinarySearch:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]


class SolutionBisect:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect(letters, target)
        return letters[index % len(letters)]


def check_cases(s: Solution):
    assert s.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert s.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert s.nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert s.nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert s.nextGreatestLetter(["c", "f", "j"], "z") == "c"
    assert s.nextGreatestLetter(["e", "e", "e", "e", "e", "n", "n", "n"], "e") == "n"


def test_solution():
    check_cases(Solution())


def test_solution_seen():
    check_cases(SolutionSeen())


def test_solution_linear():
    check_cases(SolutionLinear())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())


def test_solution_bisect():
    check_cases(SolutionBisect())
