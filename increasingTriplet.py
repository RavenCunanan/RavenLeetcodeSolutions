class Solution(object):
    def increasingTriplet(self, nums):
        first=float('inf')
        second=float('inf')

        for num in nums:
            if num<=first:
                first=num #update smallest number
            elif num <=second:
                second=num #second number greater than first
            else: #find number bigger than first and second
                return True
        
        return False
