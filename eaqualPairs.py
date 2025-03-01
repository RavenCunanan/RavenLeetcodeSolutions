class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)

        # Extract all rows
        rows =[tuple(row) for row in grid]

        # Extract all columns
        columns = [tuple(grid[i][j] for i in range(n)) for j in range(n)]

        # Count the frequency of each row and column
        from collections import defaultdict
        row_count = defaultdict(int)
        col_count = defaultdict(int)

        for row in rows:
            row_count[row] += 1
        
        for col in columns:
            col_count[col] += 1
        
        result = 0
        for key in row_count:
            if key in col_count:
                result += row_count[key] * col_count[key]
        
        return result
        
