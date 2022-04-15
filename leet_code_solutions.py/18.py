class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        
        if len(nums)<4:
            return ans
        
        nums.sort()
        #print(nums)
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):

                diff = (nums[i]+nums[j])

                low=j+1
                high=len(nums)-1
                
                while(low<high):
                    while(low<high and (low==i or low==j)):low+=1
                    while(low<high and (high==i or high==j)):high-=1
                        
                    Sum = diff + (nums[low]+nums[high])

                    if Sum==target:
                        temp=sorted([nums[i],nums[j],nums[low],nums[high]])
                        if temp not in ans:
                            ans.append(temp)

                    if Sum<target:
                        low+=1
                    else:
                        high-=1
                    
        return ans
    
