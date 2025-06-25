class Solution(object):
    def majorityElement(self, nums):
        count = 0
        major = None

        for num in nums:
            if count == 0:
                major = num
            count += (1 if num == major else -1)

        return major
