# Runtime: 148 ms, faster than 21.06% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.4 MB, less than 97.40% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=1
        while(True):
            if len(nums)==i-1:
                return i            
            while(len(nums)!=i and nums[i-1]==nums[i]):
                nums.pop(i)
            i+=1 
        return i+1
