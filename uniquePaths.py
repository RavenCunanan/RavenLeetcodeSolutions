class Solution(object):
    def uniquePaths(self, m, n):
        N = m + n - 2
        k = min(m - 1, n - 1) # Take the smaller one to minimize computation
        result = 1
        for i in range(1, k + 1):
            result = result * (N - k + i) // i
        return result    
