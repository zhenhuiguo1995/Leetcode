# the key idea is to build two heaps:
# one minheap of size k, which stores the biggest k elements
# one maxheap of size (n - k), which stores the small (n - k) elements
from heapq import *
class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.minheap = nums
        self.maxheap = []
        heapify(self.minheap)
        while len(self.minheap) > self.k:
            temp = heappop(self.minheap)
            heappush(self.maxheap, - temp)
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.minheap, val)
        if len(self.minheap) == self.k:
            return self.minheap[0]
        else:
            temp = heappop(self.minheap)
            temp = -heappushpop(self.maxheap, -temp)
            temp = heappushpop(self.minheap, temp)
            heappush(self.maxheap, -temp)
            return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)