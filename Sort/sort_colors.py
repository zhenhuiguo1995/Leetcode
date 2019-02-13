# two pointer solution
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # swap the value of two elements in an array
        def swap(a, b):
            temp = nums[b]
            nums[b] = nums[a]
            nums[a] = temp
    
        i, k = 0, len(nums) - 1
        j = 0
        while i <= k:
            if nums[i] == 0 and i != j:
                swap(i, j)
                i -= 1
                j += 1
            elif nums[i] == 2 and i != k:
                swap(i, k)
                i -= 1
                k -= 1
            i += 1