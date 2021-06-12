from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(index: int) -> int:
            visited.add(index)

            for room in rooms[index]:
                if room not in visited:
                    dfs(room)

        dfs(0)

        return len(visited) == len(rooms)


class SolutionDFS:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)

        return all(seen)


def check_solutions(rooms: List[List[int]], expect: bool):
	s = Solution()
	s_dfs = SolutionDFS()

	assert s.canVisitAllRooms(rooms) == expect
	assert s_dfs.canVisitAllRooms(rooms) == expect


if __name__ == "__main__":
	check_solutions([[1], [2], [3], []], True)
	check_solutions([[1, 3], [3, 0, 1], [2], [0]], False)
