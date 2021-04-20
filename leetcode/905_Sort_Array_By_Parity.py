from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # divide odd, even numbers
        res = []
        for num in A:
            if num % 2 == 0:
                res.insert(0, num)
            else:
                res.append(num)

        return res


class SolutionSorted:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x%2 == 1)


class SolutionListComprehension:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
