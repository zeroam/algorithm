from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        ans = base = 0
        
        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]:  # if base is a left-boundary
                # set end to the peak of this potential mountain
                while end + 1 < N and A[end] < A[end + 1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]:  # if end is really a peak
                    # set 'end' to right-boundary of muntain
                    while end + 1 < N and A[end] > A[end + 1]:
                        end += 1
                    # record candidate answer
                    ans = max(ans, end - base + 1)
                    
            base = max(end, base + 1)

        return ans
                

if __name__ == "__main__":
    s = Solution()

    A = [2, 2, 2]
    expect = 0
    assert s.longestMountain(A) == expect

    A = [2, 1, 4, 7, 3, 2, 5]
    expect = 5
    assert s.longestMountain(A) == expect

    A = [875, 884, 239, 731, 723, 685]
    expect = 4
    assert s.longestMountain(A) == expect

    A = [2, 3, 3, 2, 0, 2]
    expect = 0
    assert s.longestMountain(A) == expect

    A = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    expect = 3
    assert s.longestMountain(A) == expect
