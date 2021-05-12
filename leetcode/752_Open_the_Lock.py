from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        deadends = set(deadends)

        if target == start:
            return 0
        if start in deadends:
            return -1


        def rotate(num: str) -> str:
            num = int(num) + 10
            num_add = str((num + 1) % 10)
            num_sub = str((num - 1) % 10)
            return num_add, num_sub

        queue = [start]
        used = set(start)
        count = 0
        while queue:
            count += 1
            #print(f"level: {count}, {queue}")
            for _ in range(len(queue)):
                lock = queue.pop(0)
                for i in range(4):
                    num_add, num_sub = rotate(lock[i])

                    case1 = lock[:i] + num_add + lock[i + 1:]
                    if not (case1 in used or case1 in deadends):
                        used.add(case1)
                        if case1 == target:
                            return count
                        queue.append(case1)

                    case2 = lock[:i] + num_sub + lock[i + 1:]
                    if not (case2 in used or case2 in deadends):
                        used.add(case2)
                        if case2 == target:
                            return count
                        queue.append(case2)

        return -1


class SolutionBFS:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = deque([("0000", 0)])
        seen = set("0000")
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))

        return -1


def check_solutions(deadends: List[str], target: str, expect: int) -> None:
    s = Solution()
    s_bfs = SolutionBFS()

    assert s.openLock(deadends, target) == expect
    assert s_bfs.openLock(deadends, target) == expect


if __name__ == "__main__":
    check_solutions(["0201", "0101", "0102", "1212", "2002"], "0202", 6)
    check_solutions(["8888"], "0009", 1)
    check_solutions(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1)
    check_solutions(["1234", "2312"], "0000", 0)
