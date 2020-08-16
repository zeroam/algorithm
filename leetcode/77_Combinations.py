from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                result.append(curr[:])
                return
            
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
                
        result = []
        backtrack()
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
