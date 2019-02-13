from heapq import *
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if i * n + j < k:
                    heap.append(- matrix[i][j])
        heapify(heap)
        for i in range(k, n**2):
            row_index = i//n
            column_index = i - n * row_index
            heappushpop(heap, - matrix[row_index][column_index])
        return - heap[0]