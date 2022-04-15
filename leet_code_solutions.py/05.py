def longestPalindrome(s: str) -> str:

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expandFromMiddle(s, i, i)
        len2 = expandFromMiddle(s, i, i+1)
        length = max(len1, len2)

        if length > end - start:
            start = i - ((length - 1) // 2)
            end = i + (length // 2) + 1

    return s[start:end]


def expandFromMiddle(s: str, lower: int, higher: int) -> int:

    while lower > -1 and higher < len(s) and s[lower] == s[higher]:
        higher += 1
        lower -= 1

    return higher - lower - 1


print(longestPalindrome("ababad"))

# def longestPalindrome(s: str) -> str:
#     Max=s[0]
#     if len(s)==1 or s==s[::-1]:
#         return s

#     for left in range(len(s)):
#         right=left+len(Max)

#         while(right<len(s)):
            
#             if s[left:right+1]==s[left:right+1][::-1]:
#                 if len(Max)<len(s[left:right+1]):
#                     Max=s[left:right+1]
#             right+=1
#         #print(s[left:right+1])
#     return Max

## Slower than above
##class Solution:
##    def longestPalindrome(self, s: str) -> str:
##        Max=s[0]
##        
##        if len(s)==1 or s==s[::-1]:
##            return s
##        left=0
##        while(left<len(s)):
##            right=left+len(Max)
##
##            while(right<len(s)):
##                
##                if s[left:right+1]==s[left:right+1][::-1]:
##                    if len(Max)<len(s[left:right+1]):
##                        Max=s[left:right+1]
##                right+=1
##            if s[left:right+1]==s[left:right+1][::-1]:   
##                left=right-1
##            left+=1
##            #print(s[left:right+1])
##        return Max

#s="raedvmtyxveocfyhluuozodpxlroyjcsfslqmjthsbxhteeinpmnejxxcsyjgugclkehagpemfrnqtrkiropblcqdboztxtsaxqnsktrhzelynbzkxcghhfntrdauyzhzgujhniazijshesigzckgxentepeohcltpydumougjkmgoscchqsryaiamoujnyfpcsbwqtwikedbsjxxtnrpfgeqymwfngixslwlifimdapgzanuqwhwpesaigeoiwoyxzjmxukbsvsjvnjhwdbqzuurfolcngefdpsewrpvwivrsjnttrewkytdvvguatidyemrswpdmeqjrxgfdmcdlrcgiqdkyaaykdqigcrldcmdfgxrjqemdpwsrmeyditaugvvdtykwerttnjsrviwvprwespdfegnclofruuzqbdwhjnvjsvsbkuxmjzxyowioegiasepwhwqunazgpadmifilwlsxignfwmyqegfprntxxjsbdekiwtqwbscpfynjuomaiayrsqhccsogmkjguomudyptlchoepetnexgkczgisehsjizainhjugzhzyuadrtnfhhgcxkzbnylezhrtksnqxastxtzobdqclbporikrtqnrfmepgaheklcgugjyscxxjenmpnieethxbshtjmqlsfscjyorlxpdozouulhyfcoevxytmvdear"
# s="ccd"
# print(longestPalindrome(s))
