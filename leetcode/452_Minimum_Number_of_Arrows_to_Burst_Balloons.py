from typing import List


class SolutionUnsolved:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 포인트 정렬
        points.sort()
        print(f"points: {points}")

        # 각 포인트 별로 겹치는 포인트를 담고 있는 데이터 셋 구성
        cands = []
        x_nums = set()
        for b_index, (b_start, b_end) in enumerate(points):
            cands.append([b_index])
            for c_index, (c_start, c_end) in enumerate(points):
                if b_index == c_index:
                    continue
                    
                if b_start <= c_start <= b_end:
                    cands[b_index].append(c_index)
                    
            for x in range(b_start, b_end + 1):
                x_nums.add(x)
                    
        n = len(cands)
        x_length = len(x_nums)

        # 데이터 셋의 조합 중 최소 갯수 구하기
        used = [False] * n
        min_arrow = n
        def make_combs(start: int, count: int, x_coords: set):
            if start >= n or len(x_coords) == x_length:
                nonlocal min_arrow
                if len(x_coords) == x_length and count < min_arrow:
                    min_arrow = count
                return
            
            for i in range(start, len(cands)):
                if used[i] == True:
                    continue
                used[i] = True
                
                cands_points = cands[i]
                next_x = x_coords.copy()
                for point_index in cands_points:
                    start, end = points[point_index]
                
                    for x in range(start, end + 1):
                        next_x.add(x)
                    
                make_combs(i + 1, count + 1, next_x) 
                
                used[i] = False

        x_coords = set()
        make_combs(0, 0, x_coords)
        
        return min_arrow


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # end 기준으로 포인트 정렬 -> 무조건 없애야 하는 풍선
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
                
        return arrows


if __name__ == "__main__":
    s = Solution()

    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expect = 2
    assert s.findMinArrowShots(points) == expect

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expect = 4
    assert s.findMinArrowShots(points) == expect

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expect = 2
    assert s.findMinArrowShots(points) == expect

    points = [[1, 22334]]
    expect = 1
    assert s.findMinArrowShots(points) == expect