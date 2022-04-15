# Runtime: 184 ms, faster than 62.68% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.2 MB, less than 22.36% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n=len(matrix)
        Min=10**9+1
        
        if k==1:
            return min(min(matrix))
        
        nums=sorted([y for x in matrix for y in x])
        
        for i,val in enumerate(nums):
            #print(i,val)
            if i>0 and i%(k-1)==0:
                if Min>val:
                    Min=val
        return Min
    
