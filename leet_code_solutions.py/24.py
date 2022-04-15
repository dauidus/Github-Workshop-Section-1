# Runtime: 28 ms, faster than 85.75% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.3 MB, less than 14.85% of Python3 online submissions for Swap Nodes in Pairs.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head==None:
            return head
        if head.next==None:
            return head
    
        prev,lead=head,head.next
        prev.next=lead.next
        lead.next=prev
        head=lead
        
        
        while(prev):
            if prev==None or prev.next==None or prev.next.next==None:
                break
                
            lead=prev.next.next.next

            temp=prev.next
            prev.next=temp.next
            temp.next=lead
            prev.next.next=temp

            prev=prev.next.next
            
            
        return (head)
        
