class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng=len(s)
        start=0
        sign=1
        if leng==0:
            return 0
        while start<leng and s[start]==' ':
            start+=1
        if start<leng and (s[start]=='+' or s[start]=='-'):
            if s[start]=='-':
                sign=-1
            start+=1
        end=start
        while end<leng and (ord(s[end])>=ord("0") and ord(s[end])<=ord("9")):
            end+=1
        if start==end:
            return 0
        ret=int(s[start:end])*sign
        if ret<-2**31:
            return -2**31
        if ret> 2**31-1:
            return 2**31-1
        return (int(s[start:end])*sign)

c=Solution()
print(c.myAtoi("21474836460"))
