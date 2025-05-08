class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap - need to remove this one
                count += 1
            else:
                # No overlap - update previous end
                prev_end = intervals[i][1]
        
        return count

        
