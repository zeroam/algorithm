from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev, cur = 0, 0

        ans = 0
        zero_exist = False
        for num in nums:
            if num == 0:
                zero_exist = True
                ans = max(ans, prev + cur + 1)
                prev = cur
                cur = 0

            if num == 1:
                cur += 1

        return max(ans, prev + cur + int(zero_exist))


class SolutionBrouteForce:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        size = len(nums)

        ans = 0
        for left in range(size):
            num_zeros = 0
            for right in range(left, size):
                if num_zeros == 2:
                    break
                if nums[right] == 0:
                    num_zeros += 1

                if num_zeros <= 1:
                    ans = max(ans, right - left + 1)

        return ans


class SolutionSlidingWindow:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, 0
        num_zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros == 2:
                if nums[left] == 0:
                    num_zeros -= 1

                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


def check_solutions(nums: List[int], expect: int):
    s = Solution()
    s_bf = SolutionBrouteForce()
    s_sw = SolutionSlidingWindow()

    assert s.findMaxConsecutiveOnes(nums) == expect
    assert s_bf.findMaxConsecutiveOnes(nums) == expect
    assert s_sw.findMaxConsecutiveOnes(nums) == expect


if __name__ == "__main__":
    check_solutions([1], 1)
    check_solutions([1, 1], 2)
    check_solutions([1, 1, 0], 3)
    check_solutions([1, 1, 0, 1], 4)
    check_solutions([1, 0, 1, 1, 0], 4)
    check_solutions([1, 0, 0, 1, 1, 0], 3)
    check_solutions([1, 0, 0, 1, 1, 0, 1], 4)
