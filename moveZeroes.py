class Solution(object):
    def moveZeroes(self, nums):
        zero_index=0

        #Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[zero_index]=nums[i]
                zero_index+=1
        
        #fill remaining elements with zeros
        for i in range(zero_index, len(nums)):
            nums[i]=0
        
        return nums
