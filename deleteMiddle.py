class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: If there's only one node, return None
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None # To keep track of the node before slow

        #Move fast pointer twice as fast as slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        #Delete the middle node by skipping it
        prev.next = slow.next

        return head
