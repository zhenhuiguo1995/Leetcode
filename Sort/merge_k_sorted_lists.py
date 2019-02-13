# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
This is a classcial merge k sorted lists problem. Similar to merge sort, divide
and conquer is used in this problem.
Assume each list has at most n elements, and there are k lists, time complexity
would be O(k*logn).
T(k) = 2T(K/2) + O(n)
"""
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # merge k lists into one
        def merge_sort(lists, start, end):
            if end - start == 0:
                return lists[start]
            mid = (end - start)//2 + start
            linked_a = merge_sort(lists, start, mid)
            linked_b = merge_sort(lists, mid + 1, end)
            return merge(linked_a, linked_b)
        
        
        # merge two linked list into one and return its head
        def merge(A, B):
            if not A:
                return B
            if not B:
                return A
            p = A
            q = B
            r = None
            if p.val <= q.val:
                r = p
                p = p.next
            else:
                r = q
                q = q.next
            head = r
            while p and q:
                if p.val <= q.val:
                    r.next = p
                    p = p.next
                    r = r.next
                else:
                    r.next = q
                    q = q.next
                    r = r.next
            while p:
                r.next = p
                p = p.next
                r = r.next
            while q:
                # do
                r.next = q
                q = q.next
                r = r.next
            return head
        
        
        if not lists or len(lists) == 0:
            return lists
        return merge_sort(lists, 0, len(lists) - 1)