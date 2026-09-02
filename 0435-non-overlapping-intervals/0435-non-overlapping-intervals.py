class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # overlap → remove this interval
                count += 1
            else:
                # no overlap → keep this interval

                end = intervals[i][1]

        return count