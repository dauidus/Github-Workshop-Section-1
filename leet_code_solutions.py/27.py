
# Runtime: 28 ms, faster than 92.68% of Python3 online submissions for Remove Element.
# Memory Usage: 14.2 MB, less than 47.40% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index
