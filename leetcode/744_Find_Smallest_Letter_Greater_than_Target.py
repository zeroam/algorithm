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


def check_cases(s: Solution):
    assert s.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert s.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert s.nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert s.nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert s.nextGreatestLetter(["c", "f", "j"], "z") == "c"
    assert s.nextGreatestLetter(["e", "e", "e", "e", "e", "n", "n", "n"], "e") == "n"


def test_solution():
    check_cases(Solution())
