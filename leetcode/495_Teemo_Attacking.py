from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0
        for i in range(len(timeSeries) - 1):
            time_diff = timeSeries[i + 1] - timeSeries[i]
            if time_diff < duration:
                total_time += time_diff
            else:
                total_time += duration
                
        if len(timeSeries) > 0:
            total_time += duration

        return total_time
                

if __name__ == "__main__":
    s = Solution()

    time_series = [1, 4]
    duration = 2
    expect = 4
    assert s.findPoisonedDuration(time_series, duration) == expect

    time_series = [1, 2]
    duration = 2
    expect = 3
    assert s.findPoisonedDuration(time_series, duration) == expect

    time_series = []
    duration = 2
    expect = 0
    assert s.findPoisonedDuration(time_series, duration) == expect
