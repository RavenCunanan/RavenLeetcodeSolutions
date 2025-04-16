class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1 & 2: Node has at most one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: Node has two children
            # Find in-order successor (smallest in the right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val # Copy value
            root.right = self.deleteNode(root.right, successor.val) # Delete successor
        
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
