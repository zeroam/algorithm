from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        # make adjlist
        adj_list = [set() for _ in range(numCourses)]
        for to_node, pre_node in prerequisites:
            adj_list[to_node].add(pre_node)

        dq = deque()
        visited = [False] * numCourses
        for node, pre_nodes in enumerate(adj_list):
            if len(pre_nodes) == 0:
                dq.append(node)
                visited[node] = True


        # add queue to node which adjlist is empty
        ans = []
        while dq:
            cur_node = dq.popleft()
            print(dq, cur_node, adj_list)
            for node, pre_nodes in enumerate(adj_list):
                if visited[node]:
                    continue

                if cur_node in pre_nodes:
                    pre_nodes.remove(cur_node)
                if len(pre_nodes) == 0:
                    dq.append(node)
                    visited[node] = True

            ans.append(cur_node)

        if len(ans) != numCourses:
            return []
        return ans


def check_cases(s: Solution):
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in ([0, 1, 2, 3], [0, 2, 1, 3])
    assert s.findOrder(1, []) == [0]
    assert s.findOrder(2, [[0,1],[1,0]]) == []


def test_solution():
    check_cases(Solution())
