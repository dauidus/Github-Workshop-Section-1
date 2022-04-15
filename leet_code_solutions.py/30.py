class Solution:
    # Runtime: 680 ms, faster than 43.57% of Python3 online submissions for Substring with Concatenation of All Words.
    # Memory Usage: 14.7 MB, less than 31.24% of Python3 online submissions for Substring with Concatenation of All Words
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans=[]
        
        frequency_count=collections.Counter(words)
        max_len=len(words[0])*len(words)
        word_len=len(words[0])
        
        for i in range(len(s)-max_len+1):
            word=(s[i:i+max_len])
            breakdown=[word[i:i+word_len] for i in range(0,len(word),word_len)]
            
            if collections.Counter(breakdown)==frequency_count:
                ans.append(i)
            
        return ans
