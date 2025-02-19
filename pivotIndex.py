class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i,num in enumerate(nums): #i is index and num is value
            if left_sum == total_sum - left_sum - num: #total_sum - left_sum - num is the formula for the right sum
                return i
            left_sum += num
        
        return -1
