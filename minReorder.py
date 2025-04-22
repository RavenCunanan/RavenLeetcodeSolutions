class Solution:
    def minReorder(self, n, connections):
        from collections import defaultdict

        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))  # 1 = original direction
            graph[b].append((a, 0))  # 0 = already toward 0

        visited = set()
        res = [0]

        def dfs(node):
            visited.add(node)
            for neighbor, needs_reversal in graph[node]:
                if neighbor not in visited:
                    res[0] += needs_reversal
                    dfs(neighbor)

        dfs(0)
        return res[0]
