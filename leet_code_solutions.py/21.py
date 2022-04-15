# Runtime: 40 ms, faster than 50.67% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 29.77% of Python3 online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(0,None)
        temp=ans
        
        while(l1 and l2):
            
            if l1.val<l2.val:
                
                temp.next=ListNode(l1.val)
                temp=temp.next
                l1=l1.next
                
            elif l1.val==l2.val:
                
                temp.next=ListNode(l1.val)
                temp=temp.next
                l1=l1.next
                
                temp.next=ListNode(l2.val)
                temp=temp.next
                l2=l2.next
                
            else:
                
                temp.next=ListNode(l2.val)
                temp=temp.next
                l2=l2.next
        while(l1):
            temp.next=ListNode(l1.val)
            temp=temp.next
            l1=l1.next
        while(l2):
            temp.next=ListNode(l2.val)
            temp=temp.next
            l2=l2.next
        return ans.next
