from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0)) # row, col, steps
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r, c, steps = q.popleft()

            # Check all 4 directions
            for dr, dc in directions:
                nr, nc = r +dr, c +dc

                # If the new cell is within bounds and is an empty cell
                if 0 <= nr < rows and 0 <= nc < cols and maze [nr][nc] =='.':
                    # If it's on the border and not the enterance, return steps + 1
                    if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1) and [nr, nc] != entrance:
                        return steps + 1
                    
                    #M Mark as visited and add to queue
                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps +1))
        
        return -1
            
            
        
