from typing import List
from collections import defaultdict


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_dist(p1: List[int], p2: List[int]):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        dist_cnt = defaultdict(lambda: 0)
        dist_cnt[get_dist(p1, p2)] += 1
        dist_cnt[get_dist(p2, p3)] += 1
        dist_cnt[get_dist(p3, p4)] += 1
        dist_cnt[get_dist(p4, p1)] += 1
        dist_cnt[get_dist(p1, p3)] += 1
        dist_cnt[get_dist(p2, p4)] += 1
        
        values = list(dist_cnt.values())
        
        if len(values) != 2:
            return False
        if 2 not in values or 4 not in values:
            return False
            
        return True
        

if __name__ == "__main__":
    s = Solution()

    assert s.validSquare([0, 0], [1, 1], [1, 0], [0, 1]) == True
    assert s.validSquare([0, 0], [1, 0], [2, 0], [2, 1]) == False
    assert s.validSquare([0, 0], [5, 0], [5, 4], [0, 4]) == False
    assert s.validSquare([1, 0], [-1, 0], [0, 1], [0, -1]) == True
    assert s.validSquare([1, 0], [0, 1], [-1, 0], [0, -1]) == True
