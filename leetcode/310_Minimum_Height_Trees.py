from collections import defaultdict, deque
from re import S
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        leaves.sort()
        return leaves


class SolutionBFS:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        # make graph
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        min_depth = n - 1
        ans = []
        for i in range(n):
            # iterate bfs starts from i
            visited = set()
            queue = deque([i])
            depth = 0

            while queue:
                depth += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    visited.add(node)
                    for next_node in adj_list[node]:
                        if next_node in visited:
                            continue

                        queue.append(next_node)

            if depth < min_depth:
                min_depth = depth
                ans = [i]
            elif depth == min_depth:
                ans.append(i)

        return ans


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        # make graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining = n - len(leaves)
        while remaining > 0:
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
            remaining -= len(leaves)
        return sorted(leaves)


def check_cases(s: Solution):
    n = 1
    edges = []
    expect = [0]
    assert s.findMinHeightTrees(n, edges) == expect

    n = 2
    edges = [[0, 1]]
    expect = [0, 1]
    assert s.findMinHeightTrees(n, edges) == expect

    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    expect = [3]
    assert s.findMinHeightTrees(n, edges) == expect

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    expect = [3, 4]
    assert s.findMinHeightTrees(n, edges) == expect


def test_solution():
    check_cases(Solution())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution2():
    check_cases(Solution2())
