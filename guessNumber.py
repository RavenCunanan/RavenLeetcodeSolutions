class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
        
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else: # result == 1
                low = mid + 1
    
        return -1 # Should not reach here if the pick is guaranteed to be in [1,n]


        
