from abc import ABC, abstractmethod
import heapq
from typing import List
from collections import defaultdict


class SolutionInterface(ABC):
    @abstractmethod
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        pass


class Solution(SolutionInterface):
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)

        # make virtual node which connect cost is build well
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        # make adjacent list
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        # make edge_heap
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        mst_set = set([0])
        total_cost = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house in mst_set:
                continue

            mst_set.add(next_house)
            total_cost += cost

            # add new cost from curr_house
            for new_cost, neighbor in graph[next_house]:
                if neighbor in mst_set:
                    continue
                heapq.heappush(edges_heap, (new_cost, neighbor))

        return total_cost


def check_cases(s: SolutionInterface):
    s.minCostToSupplyWater(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]) == 3
    s.minCostToSupplyWater(2, [1, 1], [[1, 2, 1]]) == 2


def test_solution():
    check_cases(Solution())
