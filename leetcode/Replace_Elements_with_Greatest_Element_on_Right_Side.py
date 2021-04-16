from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        max_num = arr[0]
        for i in range(size):
            if max_num == arr[i]:
                max_num = -1
                for j in range(i + 1, size):
                    max_num = max(max_num, arr[j])

            arr[i] = max_num

        return arr


def check_solutions(arr: List[int], expect: List[int]):
    s = Solution()

    assert s.replaceElements(arr.copy()) == expect


if __name__ == "__main__":
    check_solutions([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])
