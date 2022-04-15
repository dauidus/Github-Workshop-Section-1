# Runtime: 440 ms, faster than 82.56% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 45.34% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        req=1
        
        if len(nums)==1:
            return True
        
        for i in range(-2,-len(nums),-1):        
            if nums[i]<req:
                req+=1
            else:
                req=1
                
        if nums[0]<req:
            return False
        return True
