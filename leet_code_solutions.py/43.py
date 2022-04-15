# Runtime: 32 ms, faster than 85.56% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.3 MB, less than 26.58% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        temp=0
        for i in range(len(num1)):
            temp+=(ord(num1[i])-48)*(10**(len(num1)-i-1))
        num1=temp
        
        temp=0
        for i in range(len(num2)):
            temp+=(ord(num2[i])-48)*(10**(len(num2)-i-1))
        num2=temp
        
        return (f"{num1*num2}")
