class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        lower_bound = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if lower_bound > start:

                count += 1
            else:
                lower_bound = end

        return count


