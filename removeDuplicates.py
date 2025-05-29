class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0 # Pointer to place the next unique element 

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1 #number of unique elements
