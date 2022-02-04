from collections import deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        degrees = [0] * n
        for src, dest in relations:
            adj_list[src - 1].append(dest - 1)
            degrees[dest - 1] += 1

        semester = 0
        courses = deque([course for course, degree in enumerate(degrees) if degree == 0])

        count = 0
        while courses:
            semester += 1
            for _ in range(len(courses)):
                course = courses.popleft()
                count += 1
                for next_course in adj_list[course]:
                    degrees[next_course] -= 1
                    if degrees[next_course] == 0:
                        courses.append(next_course)

        if count != n:
            return -1
        return semester


class SolutionDFS:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for src, dest in relations:
            adj_list[src - 1].append(dest - 1)

        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = -1
            max_length = 1
            for nei in adj_list[node]:
                length = dfs(nei)
                if length == -1:
                    return -1
                max_length = max(length + 1, max_length)

            visited[node] = max_length
            return max_length

        max_length = 1
        for node in range(n):
            length = dfs(node)
            if length == -1:
                return -1
            max_length = max(max_length, length)

        return max_length


class SolutionDFS2:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for src, dest in relations:
            adj_list[src - 1].append(dest - 1)

        visited = {}
        def check_cycle(node):
            if node in visited:
                return visited[node]

            visited[node] = True
            for nei in adj_list[node]:
                if check_cycle(nei):
                    return True

            visited[node] = False
            return False

        for node in range(n):
            if check_cycle(node):
                return -1

        visited_length = {}
        def dfs(node):
            if node in visited_length:
                return visited_length[node]

            max_length = 1
            for nei in adj_list[node]:
                length = dfs(nei)
                max_length = max(length + 1, max_length)

            visited_length[node] = max_length
            return max_length

        max_length = 1
        for node in range(n):
            length = dfs(node)
            max_length = max(max_length, length)

        return max_length


def check_cases(s: Solution):
    assert s.minimumSemesters(3, [[1, 3], [2, 3]]) == 2
    assert s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]) == -1


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_dfs2():
    check_cases(SolutionDFS2())
