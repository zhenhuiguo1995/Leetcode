# pay special attention because 0 in python is interpreted as False

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        NOCOLOR = 'nocolor'
        RED = 'red'
        BLUE = 'blue'
        color = [NOCOLOR for _ in range(len(graph))]
        if graph:
            for i in range(len(graph)):
                if color[i] == NOCOLOR:
                    queue = [i]
                    color[i] = RED
                    while queue:
                        temp = queue.pop(0)
                        for vertex in graph[temp]:
                            if color[vertex] == NOCOLOR:
                                if color[temp] == RED:
                                    color[vertex] = BLUE
                                else:
                                    color[vertex] = RED
                                queue.append(vertex)
                            elif color[vertex] == color[temp]:
                                return False            
        return True
            