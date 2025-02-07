class Solution(object):
    def longestOnes(self,nums, k):
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # When zero_count exceeds k, move the left pointer
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum window size
            max_length = max(max_length, right - left + 1)

        return max_length
