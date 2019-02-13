# classical BFS in graphs using topological sort.
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            indegree[pair[0]] += 1
            adj_list[pair[1]] += [pair[0]]
        order = []
        queue = [x for x in range(numCourses) if indegree[x] == 0]
        while queue:
            course = queue.pop(0)
            order.append(course)
            for temp in adj_list[course]:
                indegree[temp] -= 1
                if indegree[temp] == 0:
                    queue.append(temp)
                    
        return len(order) == numCourses
