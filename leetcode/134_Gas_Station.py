from typing import List


class Solution:  # O(n2) - Time Complexity
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        max_gas = -1
        max_index = -1
        for i in range(n):
            acc_gas = 0
            order = list(range(i, n)) + list(range(0, i))
            for j in order[:-1]:
                cur_cost = cost[j]
                cur_gas = gas[j]
                acc_gas += cur_gas - cur_cost
                
                if acc_gas <= 0:
                    break
                    
            if acc_gas <= 0 and len(gas) > 1:
                continue
                
            acc_gas += gas[order[-1]] - cost[order[-1]]
            
            if acc_gas > max_gas:
                max_gas = acc_gas
                max_index = i

        return max_index


class Solution1:  # O(n) - Time Complexity
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_tank, cur_tank = 0, 0
        start_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            
            if cur_tank < 0:
                start_station = i + 1
                cur_tank = 0
                
        return start_station if total_tank >= 0 else -1
    


if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()

    gas = [5]
    cost = [4]
    expect = 0
    assert s.canCompleteCircuit(gas, cost) == expect
    assert s1.canCompleteCircuit(gas, cost) == expect

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expect = 3
    assert s.canCompleteCircuit(gas, cost) == expect
    assert s1.canCompleteCircuit(gas, cost) == expect

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    expect = -1
    assert s.canCompleteCircuit(gas, cost) == expect
    assert s1.canCompleteCircuit(gas, cost) == expect
