# first solution: using quick select
# on leetcode this code is rather slow
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def swap(m, n):
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
        
        def partition(begin, end, target):
            pivot = nums[end]
            i = begin - 1
            curr = begin
            for curr in range(begin, end):
                if nums[curr] < pivot:
                    swap(i + 1, curr)
                    i += 1
            swap(i + 1, end)
            index = i + 1
            if index < target:
                return partition(index + 1, end, target)
            elif index > target:
                return partition(begin, index - 1, target)
            else:
                return nums[index]
        
        # the kth largest element is the (len(nums) - k + 1)th smallest element in the array
        return partition(0, len(nums) - 1, len(nums) - k)

# second solution: using maxHeap
# Note: in python there is no maxHeap, and the most classical way of using a 
# maxHeap is to negate all the values and use a minHeap
from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [- num for num in nums]
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)
        return - heappop(nums)

# third solution: using minHeap
# first construct a minheap of size k using the first k elements in nums
# for the next elements:
# every time push an element into the heap and pop an element from the heap,
# given the property of the heap, in the end, only the largest k elements will
# be left in the heap and the top of the heap is the element of kth rank
from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[0:k]
        heapify(heap)
        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])
        return heap[0]