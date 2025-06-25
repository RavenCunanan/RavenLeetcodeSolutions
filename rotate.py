class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums) # Handle cases where k is larger than the array length
        nums[:] = nums[-k:] + nums [:-k]
