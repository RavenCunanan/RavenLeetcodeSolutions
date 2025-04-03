class Solution(object):
    def countGoodNodes(self, node, maxVal):
        if not node:
            return 0
        
        #Check if the current node is "good"
        good = 1 if node.val >= maxVal else 0

        #Update maxVal for the next nodes in the path
        maxVal = max(maxVal, node.val)

        #Recur for left and right children
        return good + self.countGoodNodes(node.left, maxVal) + self.countGoodNodes(node.right, maxVal)

    def goodNodes(self,root):
        return self.countGoodNodes(root,root.val)
