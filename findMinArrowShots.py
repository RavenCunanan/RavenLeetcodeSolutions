class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort by xend
        points.sort(key=lambda x: x[1])

        arrow_count = 1
        current_end = points[0][1]

        for xstart, xend in points[1:]:
            if xstart > current_end:
                arrow_count += 1
                current_end = xend
        
        return arrow_count
        
