class Solution(object):
    def helper(self, l, r, s):
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return s[l+1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""

        for i in range(len(s)):
            tmp=self.helper(i,i,s)
            if len(res)<len(tmp):
                res=tmp
            tmp=self.helper(i,i+1,s)
            if len(res) <len(tmp):
                res=tmp
        return res
