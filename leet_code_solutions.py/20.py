## Runtime: 24 ms, faster than 95.82% of Python3 online submissions for Valid Parentheses.
## Memory Usage: 14.3 MB, less than 62.87% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        need = []
        
        for i in range(len(s)):
            if s[i]==')' or s[i]=='}' or s[i]==']':
                if len(need)==0:
                    return False
                
                if s[i]==need[-1]:
                    need.pop()
                else:
                    return False
                
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                
                if ord(s[i])==40:
                    need.append(chr(ord(s[i])+1))
                else:
                    need.append(chr(ord(s[i])+2))
                
        if len(need)==0:
            return True
        return False
