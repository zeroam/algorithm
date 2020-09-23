from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n / 3
        
        counter = dict()
        result = set()
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1

            if counter[num] > limit:
                result.add(num)

        return list(result)


class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        # 2dn pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
                
        return result


if __name__ == "__main__":
    s = Solution()
    s1 = Solution()

    nums = [3, 2, 3]
    expect = [3]
    assert s.majorityElement(nums) == expect
    assert s1.majorityElement(nums) == expect

    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    expect = [1, 2]
    assert s.majorityElement(nums) == expect
    assert s1.majorityElement(nums) == expect
