class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0

        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i - 1]
            total_time += min(gap, duration)

        total_time += duration

        return total_time