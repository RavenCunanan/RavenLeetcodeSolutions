class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even # Store the start of even nodes

        while even and even.next:
            odd.next = even.next
            odd = odd.next # Move odd forward

            even.next = odd.next
            even = even.next #Move even forward

        odd.next = even_head # Attach even list to the end of odd list
        return head
