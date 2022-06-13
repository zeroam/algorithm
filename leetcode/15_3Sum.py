from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i -1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return results


class SolutionTwoSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i -1]:
                continue

            result.extend(self.twoSum(i, nums))

        return result

    def twoSum(self, i: int, nums: List[int]) -> List[int]:
        result = []
        seen = set()

        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])
            j += 1

        return result


def check_cases(s: Solution):
    s.threeSum([]) == []
    s.threeSum([0]) == []
    s.threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_solution():
    check_cases(Solution())


def test_solution_two_sum():
    check_cases(SolutionTwoSum())
