class Solution(object):
    def largestAltitude(self, gain):
        largeAlt=0 # Tracks the highest altitude
        currentPos=0 # Tracks the cumulative altitude

        for i in gain: # Iterate over the values in gain
            currentPos+=i # Update cumulative altitude
            largeAlt=max(largeAlt,currentPos) # Update highest altitude
        
        return largeAlt  # Return the highest altitude
