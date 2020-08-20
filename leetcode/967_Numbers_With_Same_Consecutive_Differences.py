from collections import deque
from typing import List


class DFSSolution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        
        ans = []
        def dfs(N: int, num: int): 
            if N == 0:
                ans.append(num)
                return
            
            tail_digit = num % 10
            next_digits = set([tail_digit - K, tail_digit + K])
            
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    next_num = num * 10 + next_digit
                    dfs(N - 1, next_num)
            
        for num in range(1, 10):
            dfs(N - 1, num)
            
        return ans


class BFSSolution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        
        ans = []
        dq = deque()
        for num in range(1, 10):
            dq.append((num, 1))
            
        while dq:
            num, level = dq.popleft()
            
            if level == N:
                ans.append(num)
                continue
            
            tail_digit = num % 10
            next_digits = set([tail_digit - K, tail_digit + K])
            
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    next_num = num * 10 + next_digit
                    dq.append((next_num, level + 1))
            
        return ans


if __name__ == "__main__":
    ds = DFSSolution()
    bs = BFSSolution()
    
    case1 = (3, 7)
    assert ds.numsSameConsecDiff(*case1) == [181, 292, 707, 818, 929]
    assert bs.numsSameConsecDiff(*case1) == [181, 292, 707, 818, 929]
