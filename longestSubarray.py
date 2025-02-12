class Solution(object):
    def longestSubarray(self, nums):
        left=0
        maxLength=0
        zeroCount=0

        # Count the number of 0s in the current window as the right pointer expands.
        for right in range(len(nums)):
            if nums[right]==0:
                zeroCount+=1
            
            # If there are more than one 0, move the left pointer
            while zeroCount > 1:
                if nums[left]==0:
                    zeroCount-=1
                left+=1
            # Update the maximum length    
            maxLength=max(maxLength,right-left)
        
        # If the entire array is 1's, we must delete one element
        if maxLength==len(nums):
            return maxLength

        return maxLength
