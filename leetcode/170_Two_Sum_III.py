from collections import defaultdict


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        self.sums = set()


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        for num in self.nums:
            self.sums.add(num + number)
        self.nums.add(number)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.sums


class TwoSumSortedList:
    def __init__(self):
        self.nums = []
        self.is_sort = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sort = False


    def find(self, value: int) -> bool:
        if not self.is_sort:
            self.nums.sort()
            self.is_sort = True

        low, high = 0, len(self.nums) - 1
        while low < high:
            cur_sum = self.nums[low] + self.nums[high]
            if cur_sum < value:
                low += 1
            elif cur_sum > value:
                high -= 1
            else:
                return True
        return False


class TwoSumHashTable:
    def __init__(self):
        self.nums = defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for num in self.nums.keys():
            other = value - num
            if other in self.nums:
                if num == other and self.nums[num] == 1:
                    continue
                return True

        return False
