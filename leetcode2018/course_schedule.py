class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [-1 for _ in range(numCourses)]
        adjacent_list = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            cur, pre = pair[0], pair[1]
            adjacent_list[cur].append(pre)
        
        def dfs(index, visited):
            visited[index] = 0
            for node in adjacent_list[index]:
                if visited[node] == -1:
                    dfs(node, visited)
                elif visited[node] == 0:
                    return False
            visited[index] = 1
            
        for i in range(numCourses):
            if visited[i] == -1:
                dfs(i, visited)
        if sum(visited) != numCourses:
            return False
        else:
            return True