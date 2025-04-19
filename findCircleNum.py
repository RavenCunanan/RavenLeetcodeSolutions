class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        province_count = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                province_count += 1
        
        return province_count
