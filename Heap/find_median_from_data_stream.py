# define two heaps, maxHeap and minHeap
# maxHeap stores the small part of the data
# minHeap stores the large part of the data
# median = (top of maxHeap + top of minHeap) /2
# in addNum, we try to maintain the property of the two heaps
from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        # the key operation is to maintain the property of the two heaps
        heappush(self.large, num)
        temp = heappop(self.large)
        heappush(self.small, - temp)
        if len(self.large) < len(self.small):
            temp = heappop(self.small)
            heappush(self.large, - temp)
        
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2
        else:
            return float(self.large[0])