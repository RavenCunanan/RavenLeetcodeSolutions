from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(node, current_sum):
            if not node:
                return 0

            # Update the current sum
            current_sum += node.val

            # Check if there is a prefix sum that satisfies current_sum - targetSum
            count = prefix_sums[current_sum - targetSum]

            # Store the current sum in the map
            prefix_sums[current_sum] += 1

            # Recur to the left and right children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtrack: remove the current sum before returning to the parent
            prefix_sums[current_sum] -= 1

            return count

        # Initialize prefix sums dictionary inside the function
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle cases where the path itself equals targetSum

        return dfs(root, 0)
