class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, target):
            if len(path) == k and target == 0:
                result.append(path[:])
                return
            if len(path) > k or target < 0:
                return
            
            for i in range(start, 10): # numbers 1 through 9
                path.append(i)
                backtrack(i + 1, path, target - i)
                path.pop()
        
        backtrack(1, [], n)
        return result
