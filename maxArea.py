class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            # Calculate the current area
            current_area = min(height[start], height[end]) * (end - start)
            # Update max_area if the current area is greater
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
