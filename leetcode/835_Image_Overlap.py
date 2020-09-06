from typing import List


class Solution:
        
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dim = len(A)
        
        def shift_and_count(x_shift, y_shift, M, R):
            """
            Shift the matrix M, and count the ones in the overlapping zone
            M: matrix to be moved
            R: matrix for reference
            
            moving one matrix up and left is equivalent to
            moving the other matrix down and right
            """
            count = 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and R[r_row][r_col] == 1:
                        count += 1
            return count
        
        max_overlaps = 0
        for y_shift in range(dim):
            for x_shift in range(dim):
                max_overlaps = max(shift_and_count(x_shift, y_shift, A, B), max_overlaps)
                max_overlaps = max(shift_and_count(x_shift, y_shift, B, A), max_overlaps)
        
        return max_overlaps


if __name__ == "__main__":
    s = Solution()

    A = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    B = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
    ]
    expect = 3
    assert s.largestOverlap(A, B) == expect
