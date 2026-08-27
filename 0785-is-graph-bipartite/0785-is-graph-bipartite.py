class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)
        def dfs(node , color):
            colors[node] =color
            for neigh in graph[node]:
                if colors[neigh] == color :
                    return False
                    
                if colors[neigh] == -1:
                   if not dfs( neigh , 1-color):
                       return False
            return True

        #multiple components    
        for node in range(len(graph)):
            if colors[node] ==-1:
                if not dfs(node ,0):
                    return False
        return True            