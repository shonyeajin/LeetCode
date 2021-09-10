class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_length=len(s)
        if s_length==0 or s_length==1:
            return 0
        dp=[]
        ret=0
        for i in range(s_length):
            if s[i]=='(':
                dp.append(i)
            elif len(dp)!=0 and s[dp[-1]]=='(':
                del dp[-1]
                if len(dp)==0:
                    ret=i+1
                else:
                    ret=max(ret, i-dp[-1])
            else:
                dp.append(i)
        return ret
                

c=Solution()
print(c.longestValidParentheses(")()())"))
