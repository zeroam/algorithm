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


def check_cases(s: Solution):
    assert s.minimumSemesters(3, [[1, 3], [2, 3]]) == 2
    assert s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]) == -1


def test_solution():
    check_cases(Solution())
