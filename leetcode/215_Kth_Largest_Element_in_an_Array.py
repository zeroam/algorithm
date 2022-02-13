import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            print(nums[i], min_heap[0])
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]


class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, kth_smallest):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if kth_smallest == pivot_index:
                return nums[kth_smallest]
            elif kth_smallest < pivot_index:
                return select(left, pivot_index - 1, kth_smallest)
            else:
                return select(pivot_index + 1, right, kth_smallest)

        return select(0, len(nums) - 1, len(nums) - k)


def check_cases(s: Solution):
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([-1, 2, 0], 1) == 2


def test_solution():
    check_cases(Solution())


def test_solution_quickselect():
    check_cases(SolutionQuickSelect())
