from collections import defaultdict, deque
class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build the graph
        for (a,b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a,1 / val))

        def dfs(start, end, visited, acc):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return acc
            visited.add(start)
            for neighbor, val in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited, acc * val)
                    if result != -1.0:
                        return result
            return -1.0
        
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set(), 1.0))
        return results
        
        
