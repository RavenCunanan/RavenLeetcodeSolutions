class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()  # Sort the list to use the two-pointer technique
        start = 0
        end = len(nums) - 1
        total = 0

        while start < end:
            current_sum = nums[start] + nums[end]
            if current_sum == k:  # Found a pair
                total += 1
                start += 1  # Move to the next pair
                end -= 1
            elif current_sum < k:  # Sum is too small, move start forward
                start += 1
            else:  # Sum is too large, move end backward
                end -= 1

        return total
