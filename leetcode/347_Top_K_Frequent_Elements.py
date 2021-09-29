import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x[0] for x in c.most_common(k)]


class SolutionQuickSelect:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_freq = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all more frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] >= pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right) -> None:
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k == pivot_index + 1:
                return
            elif k < pivot_index + 1:
                # go left
                quickselect(left, pivot_index - 1)
            else:
                # go right
                quickselect(pivot_index + 1, right)

        quickselect(0, len(unique) - 1)
        return unique[:k]


def check_cases(s: Solution):
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert (
        sorted(
            s.topKFrequent(
                [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9],
                5,
            )
        )
        == [2, 3, 4, 8, 9]
    )


def test_solution():
    check_cases(Solution())


def test_solution_quick_select():
    check_cases(SolutionQuickSelect())