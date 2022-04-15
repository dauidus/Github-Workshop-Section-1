# Runtime: 224 ms, faster than 36.53% of Python3 online submissions for Shortest Palindrome.
# Memory Usage: 14.7 MB, less than 39.68% of Python3 online submissions for Shortest Palindrome.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s):
            if len(s)<2:
                return True if s else False
            if s[:len(s)//2][::-1]==s[len(s)//2+(len(s)%2):]:
                return True
            return False
        
        if isPalindrome(s):
            return s
        
        for i in range(len(s)-1,1,-1):
            if isPalindrome(s[:i]):
                #print(s[i:][::-1]+s)
                return s[i:][::-1]+s
        else:
            return s[1:][::-1]+s
