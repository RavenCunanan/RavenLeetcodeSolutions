from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Initialize the queue with all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid [r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0 # No fresh oranges to rot
        
        minutes = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Step 2: BFS
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c +dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        
        return minutes if fresh == 0 else -1

        
