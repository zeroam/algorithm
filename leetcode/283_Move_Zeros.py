from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pos = 0
        for read_pos in range(len(nums)):
            if nums[read_pos] != 0:
                nums[write_pos] = nums[read_pos]
                write_pos += 1

        # fill zeros
        for i in range(write_pos, len(nums)):
            nums[i] = 0


class SolutionCopy:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        ans = []
        zero_cnt = 0
        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                zero_cnt += 1


        for _ in range(zero_cnt):
            ans.append(0)

        for i in range(size):
            nums[i] = ans[i]


def check_solutions(nums: List[int], expect: List[int]):
    s = Solution()
    s_c = SolutionCopy()

    nums_copy = nums.copy()
    s.moveZeroes(nums_copy)
    assert nums_copy == expect

    nums_copy = nums.copy()
    s_c.moveZeroes(nums_copy)
    assert nums_copy == expect


if __name__ == "__main__":
    check_solutions([0], [0])
    check_solutions([0, 1], [1, 0])
    check_solutions([0, 1, 0], [1, 0, 0])
    check_solutions([0, 0, 1], [1, 0, 0])
    check_solutions([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
