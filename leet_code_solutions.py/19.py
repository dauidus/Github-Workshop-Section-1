class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        follow=head
        lead=head
        
        for _ in range(n):
            lead=lead.next
        if not lead:
            return head.next
        while(lead.next):
            lead=lead.next
            follow=follow.next
    
        follow.next=follow.next.next
        
        return head
