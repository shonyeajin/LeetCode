class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet=set()
        l=maxLen=0

        if len(s)==0:
            return (0)

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[i])
            maxLen=max(maxLen, i-l+1)
        return (maxLen)

            


c=Solution()
print(c.lengthOfLongestSubstring("abcabc"))



        