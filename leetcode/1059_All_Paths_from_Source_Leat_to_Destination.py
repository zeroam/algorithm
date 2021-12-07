from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # make graph
        self.graph = graph = defaultdict(list)
        for a, b in edges:
            if a == b:
                return False
            graph[a].append(b)

        # make visited
        self.visited = set([source])

        return self.backtracking(source, destination)

    def backtracking(self, cur_node, destination):
        # return True it ends with destination
        neighbors = self.graph[cur_node]
        if not neighbors:
            if cur_node == destination:
                return True
            return False

        for next_node in neighbors:
            if next_node in self.visited:
                return False

            self.visited.add(next_node)
            ret = self.backtracking(next_node, destination)
            self.visited.remove(next_node)

            if not ret:
                return ret

        return True



def check_cases(s: Solution):
    assert s.leadsToDestination(n=3, edges=[[0, 1], [0, 2]], source=0, destination=2) == False
    assert s.leadsToDestination(n=4, edges=[[0, 1], [0, 3], [1, 2], [2, 1]], source=0, destination=3) == False
    assert s.leadsToDestination(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]], source=0, destination=3) == True
    assert s.leadsToDestination(n=3, edges=[[0, 1], [1, 1], [1, 2]], source=0, destination=2) == False
    assert s.leadsToDestination(n=2, edges=[[0, 1], [1, 1]], source=0, destination=1) == False
    assert s.leadsToDestination(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]], source=0, destination=3) == False


def test_solution():
    check_cases(Solution())
