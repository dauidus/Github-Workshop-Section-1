# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Runtime: 52 ms, faster than 52.23% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 15.8 MB, less than 6.55% of Python3 online submissions for Reverse Nodes in k-Group.
# Very bad solution, pure brute-force monkey type. 

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head==None:
            return head
        if head.next==None:
            return head
        
        temp=head
        
        ans=[]
        while(temp):
            ans.append(temp.val)
            temp=temp.next
        
        n=len(ans)
        
        for i in range(n//k):
            ans[i*k:(i+1)*k]=(ans[i*k:(i+1)*k][::-1])
        
        head=temp=ListNode(ans[0],None)
        
        for i in range(1,len(ans)):
            temp.next=ListNode(ans[i],None)
            temp=temp.next
        return (head)
