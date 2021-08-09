


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        lower_end=points[0][1]
        count=0
        for start,end in points[1:]:
            if lower_end<start:
                count+=1
                lower_end=end
        return count



