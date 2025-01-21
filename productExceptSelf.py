class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        result=[1]*n #initalize the result array with 1s

        #calculate left products
        left_product=1
        for i in range(n):
            result[i]=left_product
            left_product *=nums[i]
        
        #calculate right products
        right_product=1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product*=nums[i]
        
        return result
