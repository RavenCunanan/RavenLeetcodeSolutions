class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = 0, 0 #dp[i-1], dp[i-2]

        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        
        return prev1
