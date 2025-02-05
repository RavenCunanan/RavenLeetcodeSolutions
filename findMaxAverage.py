class Solution(object):
    def findMaxAverage(self,nums, k):
        window_sum = sum(nums[:k])  # Sum of the first window
        max_sum = window_sum  # Initialize max_sum with the first window's sum

        # Slide the window from the beginning to the end of the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Update the window sum
            max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is greater

        # Return the maximum average
        return max_sum/float(k)
