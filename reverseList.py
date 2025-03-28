class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next # Store the next node
            curr.next = prev # Reverse the link
            prev = curr # Move prev to current node
            curr = next_node # Move to next node

        return prev # New head of the reversed list
