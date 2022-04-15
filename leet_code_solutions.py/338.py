
# 5 % Faster and 98% less memory

class Solution:
  def countBits(self, n: int) -> List[int]:
      ans=[0,1]

      if n<2:
          return ans[:n+1]

      for i in range(2,n+1):
          temp=i
          ans.append(0)
          for j in range(31,-1,-1):
              if temp>1<<j:
                  ans[i]+=ans[1<<j]
                  temp-=1<<j
              if temp==1<<j:
                  ans[i]+=1
                  temp=0
      return ans 
