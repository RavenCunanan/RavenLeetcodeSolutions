class Solution:
    def longestZigZag(self, root):
        self.max_length = 0

        def dfs(node):
            if not node:
                return (-1, -1)  # base case: no ZigZag

            left = dfs(node.left)
            right = dfs(node.right)

            # left[1] means the length of ZigZag ending with a right move at left child
            # right[0] means the length of ZigZag ending with a left move at right child
            self.max_length = max(self.max_length, left[1] + 1, right[0] + 1)

            return (left[1] + 1, right[0] + 1)

        dfs(root)
        return self.max_length
