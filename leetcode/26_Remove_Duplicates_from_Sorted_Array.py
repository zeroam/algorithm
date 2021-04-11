from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = None
        for j in range(len(nums)):
            if prev != nums[j]:
                prev = nums[j]
                nums[i] = nums[j]
                i += 1

        return i

def check_solution(nums: List[int], expect: List[int]):
    solutions = [Solution()]

    for s in solutions:
        nums_copy = nums.copy()
        size = s.removeDuplicates(nums_copy)
        assert nums_copy[:size] == expect


if __name__ == "__main__":
    check_solution([1, 2, 2, 3, 4], [1, 2, 3, 4])
    check_solution([1, 2, 3, 4], [1, 2, 3, 4])
    check_solution([1, 3, 3, 4], [1, 3, 4])
    check_solution([1, 1, 1, 3, 3, 4, 5, 5], [1, 3, 4, 5])

