from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            else:
                hash_set.add(num)

        return list(hash_set)[0]



def test_solution():
    s = Solution()

    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
