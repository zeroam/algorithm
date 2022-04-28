class ArrayReader:
   def get(self, index: int) -> int:
       pass


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10 ** 4
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
