# Runtime: 32 ms, faster than 77.54% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.4 MB, less than 81.36% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
    
        return haystack.index(needle) if needle in haystack else -1
