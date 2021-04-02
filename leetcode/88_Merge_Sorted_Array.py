from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def insert_one(arr, index, num):
            n = len(arr)
            for i in range(n - 2, index - 1, -1):
                arr[i + 1] = arr[i]

            arr[index] = num

        index1 = 0
        index2 = 0
        while index1 < m and index2 < n:
            num1 = nums1[index1]
            num2 = nums2[index2]
            if num1 >= num2:
                insert_one(nums1, index1, num2)
                m += 1
                index2 += 1

            index1 += 1

        while index2 < n:
            num2 = nums2[index2]
            insert_one(nums1, index1, num2)
            index1 += 1
            index2 += 1


class SolutionMergeAndSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()


class SolutionThreePointers:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()

        p1 = 0
        p2 = 0
        for i in range(m + n):
            if p2 >= n or (p1 < m and nums1_copy[p1] < nums2[p2]):
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1


class SolutionThreePointers2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1


def check_solution(nums1: List[int], m: int, nums2: List[int], n: int, expect: List[int]):
    s = Solution()
    s_ms = SolutionMergeAndSort()
    s_t = SolutionThreePointers()
    s_t2 = SolutionThreePointers2()

    nums = nums1.copy()
    s.merge(nums, m, nums2, n)
    assert nums == expect

    nums = nums1.copy()
    s_ms.merge(nums, m, nums2, n)
    assert nums == expect

    nums = nums1.copy()
    s_t.merge(nums, m, nums2, n)
    assert nums == expect

    nums = nums1.copy()
    s_t2.merge(nums, m, nums2, n)
    assert nums == expect


if __name__ == "__main__":
    check_solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    check_solution([1], 1, [], 0, [1])
