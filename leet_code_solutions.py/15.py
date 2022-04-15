
def threeSum( nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans=[]

    for i in range(len(nums)-2):
            if (i==0) or not (nums[i]==nums[i-1]):
                    low=i+1
                    high=len(nums)-1
                    k=-(nums[i])
                    while(high>low):
                            if (nums[low]+nums[high])==k:
                                    ans.append([nums[i],nums[low],nums[high]])
                                    while(low<high and nums[low]==nums[low+1]): low+=1
                                    while(low<high and nums[high]==nums[high-1]):high-=1
                                    high-=1
                                    low+=1
                            elif (nums[low]+nums[high]>k):high-=1
                            else: low+=1
    return ans
print(threeSum([[-1,0,1,2,-1,-4]))
