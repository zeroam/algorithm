from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = [None, None, None]

        for num in nums:
            if num in max_nums:
                continue
            elif max_nums[0] is None or num > max_nums[0]:
                max_nums[2] = max_nums[1]
                max_nums[1] = max_nums[0]
                max_nums[0] = num
            elif max_nums[1] is None or num > max_nums[1]:
                max_nums[2] = max_nums[1]
                max_nums[1] = num
            elif max_nums[2] is None or num > max_nums[2]:
                max_nums[2] = num

        return max_nums[2] if max_nums[2] != None else max_nums[0]


class SolutionSetAndDelete:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        maximum = max(nums)
        if len(nums) < 3:
            return maximum

        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)


class SolutionSeenMax:
    def thirdMax(self, nums: List[int]) -> int:
        def ignore_seen_max(nums, seen_max):
            maximum = None
            for num in nums:
                if num in seen_max:
                    continue
                if maximum == None or num > maximum:
                    maximum = num

            return maximum

        seen_max = set()

        for _ in range(3):
            cur_max = ignore_seen_max(nums, seen_max)
            if cur_max == None:
                return max(seen_max)

            seen_max.add(cur_max)

        return min(seen_max)


class SolutionSet:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = set()
        for num in nums:
            maximum.add(num)
            if len(maximum) > 3:
                maximum.remove(min(maximum))

        if len(maximum) == 3:
            return min(maximum)
        return max(maximum)


def check_solutions(nums: List[int], expect: int):
    solutions = [Solution(), SolutionSetAndDelete(), SolutionSeenMax(), SolutionSet()]

    for s in solutions:
        assert s.thirdMax(nums) == expect


if __name__ == "__main__":
    check_solutions([1, 2, 3], 1)
    check_solutions([1, 1, 3], 3)
    check_solutions([1, 5, -12], -12)
    check_solutions([2, 2, 3, 1], 1)
