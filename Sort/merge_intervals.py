class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) > 1:
            intervals = sorted(intervals, key=lambda x:x.start)
            result = []
            start, end = intervals[0].start, intervals[0].end
            for interval in intervals:
                # if overlapping intervals exists, move end as needed
                if interval.start <= end:
                    end = max(interval.end, end)
                # if not, append the interval to result
                else:
                    result.append(Interval(start, end))
                    start, end = interval.start, interval.end
            
            # add the last interval
            result.append(Interval(start, end))
            return result
            
        return intervals