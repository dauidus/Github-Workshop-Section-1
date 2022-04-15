# Runtime: 24 ms, faster than 99.78% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 48.08% of Python3 online submissions for Flatten Binary Tree to Linked List.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def flatten(root):
            temp=None
            if root.right:
                flatten(root.right)
                temp=root.right
            if root.left:
                root.right,root.left=root.left,None
                flatten(root.right)
                while(root.right):
                    root=root.right
                if temp:
                    root.right=temp
        flatten(root)
