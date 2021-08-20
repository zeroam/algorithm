from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # swap if nums1 is longer than nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # sort
        nums1.sort()
        nums2.sort()

        result = []
        index = 0
        for i, val1 in enumerate(nums1):
            for j in range(index, len(nums2)):
                val2 = nums2[j]
                if val1 == val2:
                    result.append(val1)
                    index = j + 1
                    break
                elif val2 > val1:
                    index = j
                    break

        return result


class SolutionCounter:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # swap if nums1 is longer than nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # nums1 to counter
        counter = {}
        for num in nums1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        result = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1

        return result


def check_cases(s: Solution):
    assert sorted(s.intersect([1, 2, 2, 1], [2, 2])) == sorted([2, 2])
    assert sorted(s.intersect([4, 9, 5], [9, 4, 9, 8, 4])) == sorted([4, 9])
    assert sorted(s.intersect([2, 5, 4, 8, 7], [1, 1, 9, 2, 2])) == sorted([2])


def test_solution():
    check_cases(Solution())


def test_solution_counter():
    check_cases(SolutionCounter())
