from collections import deque
from typing import List


class SolutionDFS:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        return self.dfs(maze, start, destination, visited)
    
    def dfs(self, maze: List[List[int]], start: List[int], destination: List[int], visited: List[List[int]]) -> bool:
        if visited[start[0]][start[1]]:
            return False
        
        if start[0] == destination[0] and start[1] == destination[1]:
            return True
        
        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited[start[0]][start[1]] = True

        for d_x, d_y in direction:
            x = start[0] + d_x
            y = start[1] + d_y
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                x += d_x
                y += d_y

            if self.dfs(maze, [x - d_x, y - d_y], destination, visited):
                return True
        
        return False


class SolutionBFS:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        dq = deque()
        dq.append(start)
        visited[start[0]][start[1]] = True
        while dq:
            s_x, s_y = dq.popleft()
            if s_x == destination[0] and s_y == destination[1]:
                return True
            
            for d_x, d_y in direction:
                x = s_x + d_x
                y = s_y + d_y
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += d_x
                    y += d_y
                    
                if visited[x - d_x][y - d_y] == False:
                    dq.append([x - d_x, y - d_y])
                    visited[x - d_x][y - d_y] = True
                    
        return False
        

if __name__ == "__main__":
    s_dfs = SolutionDFS()
    s_bfs = SolutionBFS()

    case1 = {
        "maze": [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
        "start": [0, 4],
        "destination": [4, 4] 
    }
    expect1 = True
    assert s_dfs.hasPath(**case1) == expect1
    assert s_bfs.hasPath(**case1) == expect1

    case2 = {
        "maze": [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
        "start": [0, 4],
        "destination": [3, 2]
    }
    expect2 = False
    assert s_dfs.hasPath(**case2) == expect2
    assert s_bfs.hasPath(**case2) == expect2
