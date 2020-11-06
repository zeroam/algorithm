from collections import Counter
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = Counter(position)
        sorted_counter = counter.most_common()
        
        odd_handled = False
        even_handled = False
        odd_cost = 0
        even_cost = 0
        print(sorted_counter)
        for k, v in sorted_counter:
            if k % 2 == 1 and odd_handled == False:
                # handling odd number
                for k2, v2 in sorted_counter:
                    if abs(k2 - k) % 2 == 1:
                        odd_cost += v2
                odd_handled = True
            elif k % 2 == 0 and even_handled == False:
                # handling even number
                for k2, v2 in sorted_counter:
                    if abs(k2 - k) % 2 == 1:
                        even_cost += v2
                even_handled = True
                
            if odd_handled and even_handled:
                break
            
        print(f"odd_cost: {odd_cost}")
        print(f"even_cost: {even_cost}")
        
        result: int
        if odd_handled == False:
            result = even_cost
        elif even_handled == False:
            result = odd_cost
        else:
            result = min(even_cost, odd_cost)
        
        return result


class SolutionOrigin:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_cost = 0
        odd_cost = 0
        
        for pos in position:
            if pos % 2 == 0:
                even_cost += 1
            else:
                odd_cost += 1
                
        return min(even_cost, odd_cost)


if __name__ == "__main__":
    s = Solution()
    s_o = SolutionOrigin()

    position = [2, 2, 2, 3, 3]
    expect = 2
    assert s.minCostToMoveChips(position) == expect
    assert s_o.minCostToMoveChips(position) == expect

    position = [10, 3, 3, 1, 6, 2, 1, 10, 6, 6]
    expect = 4
    assert s.minCostToMoveChips(position) == expect
    assert s_o.minCostToMoveChips(position) == expect
