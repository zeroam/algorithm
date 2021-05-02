from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        WALL = -1
        GATE = 0
        EMPTY = 2147483647
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        m = len(rooms)
        n = len(rooms[0])

        def get_nearest_gate(y: int, x: int) -> int:
            start = rooms[y][x]
            if start != EMPTY:
                return start

            queue = [(y, x)]
            visited = set()
            step = 0

            while queue:
                size = len(queue)
                step += 1
                for _ in range(size):
                    cur_y, cur_x = queue.pop(0)
                    visited.add((cur_y, cur_x))

                    for dir_y, dir_x in DIRECTIONS:
                        new_y = cur_y + dir_y
                        new_x = cur_x + dir_x

                        if new_y < 0 or new_y >= m or new_x < 0 or new_x >= n:
                            continue
                        if (new_y, new_x) in visited:
                            continue

                        new_value = rooms[new_y][new_x]
                        if new_value == GATE:
                            return step
                        elif new_value != WALL:
                            queue.append((new_y, new_x))

            return start

        for y in range(m):
            for x in range(n):
                rooms[y][x] = get_nearest_gate(y, x)


class SolutionFromGate:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        WALL = -1
        GATE = 0
        EMPTY = 2147483647
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        m = len(rooms)
        n = len(rooms[0])

        queue = []
        step = 0

        # add gates from start
        for y in range(m):
            for x in range(n):
                if rooms[y][x] == GATE:
                    queue.append((y, x))

        while queue:
            step += 1
            for _ in range(len(queue)):
                cur_y, cur_x = queue.pop(0)

                for dir_y, dir_x in DIRECTIONS:
                    new_y = cur_y + dir_y
                    new_x = cur_x + dir_x

                    # invalid range of new_y, new_x
                    if new_y < 0 or new_y >= m or new_x < 0 or new_x >= n:
                        continue

                    # invalid value of new_y, new_x
                    new_value = rooms[new_y][new_x]
                    if new_value == WALL or new_value != EMPTY:
                        continue

                    queue.append((new_y, new_x))
                    rooms[new_y][new_x] = rooms[cur_y][cur_x] + 1
