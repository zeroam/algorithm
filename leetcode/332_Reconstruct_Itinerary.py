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


class SolutionHierholzers:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        self.graph = defaultdict(list)

        visited = {}
        for origin, dest in tickets:
            self.graph[origin].append(dest)

        # sort the itinerary based on lexical order
        for origin, itinerary in self.graph.items():
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS(start)

        return self.result[::-1]

    def DFS(self, origin):
        dest_list = self.graph[origin]
        while dest_list:
            next_dest = dest_list.pop()
            self.DFS(next_dest)

        self.result.append(origin)


class SolutionIteration:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            routes[start].append(end)

        result, stack = [], ["JFK"]
        while stack:
            while routes[stack[-1]]:
                stack.append(routes[stack[-1]].pop())
            result.append(stack.pop())

        return result[::-1]


def check_cases(s: Solution):
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    output = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert s.findItinerary(tickets) == output

    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    output = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert s.findItinerary(tickets) == output

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    output = ["JFK", "NRT", "JFK", "KUL"]
    assert s.findItinerary(tickets) == output


def test_solution():
    check_cases(Solution())


def test_solution_hieholzers():
    check_cases(SolutionHierholzers())


def test_solution_iteration():
    check_cases(SolutionIteration())
