import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(float(pile) / mid) for pile in piles)

            if hours > h:
                left = mid + 1 # Need to eat faster
            else:
                right = mid # Try slower speed
        
        return left
        
