from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        graph = defaultdict(list)

        visited = {}
        for origin, dest in tickets:
            graph[origin].append(dest)

        # sort the itinerary based on lexical order
        for origin, itinerary in graph.items():
            itinerary.sort()
            visited[origin] = [False] * len(itinerary)

        result = []
        def backtracking(origin, route):
            if len(route) == len(tickets) + 1:
                nonlocal result
                result = route.copy()
                return True

            for i, next_dest in enumerate(graph[origin]):
                if visited[origin][i]:
                    continue

                visited[origin][i] = True
                route.append(next_dest)
                ret = backtracking(next_dest, route)
                visited[origin][i] = False
                route.pop()
                if ret:
                    return True

            return False

        backtracking(start, [start])
        return result


def check_cases(s: Solution):
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    output = ["JFK","MUC","LHR","SFO","SJC"]
    assert s.findItinerary(tickets) == output

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    output = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert s.findItinerary(tickets) == output

    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    output = ["JFK","NRT","JFK","KUL"]
    assert s.findItinerary(tickets) == output


def test_solution():
    check_cases(Solution())
