
def threeSumClosest(nums: List[int], target: int) -> int:

        nums.sort()
        Min=10**4

        for i in range(len(nums)-1):
            low=i+1
            high=len(nums)-1

            while(low<high):
                diff = abs(nums[i]+nums[low]+nums[high]-target)

                if diff==0:
                    return nums[i]+nums[low]+nums[high]

                if diff<=Min:
                    ans = nums[i] + nums[low] + nums[high]
                    Min = diff

                if nums[i]+nums[low]+nums[high]<=target:
                    low+=1
                else:
                    high-=1
        return ans
print(threeSumClosest([[-1,2,1,-4]))
