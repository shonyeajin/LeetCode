class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a=abs(dividend)
        b=abs(divisor)
        ret=0
        while a>=b:
            temp=b
            mul=1
            while a>=temp:
                a-=temp
                temp+=temp
                ret+=mul
                mul+=mul
        if ((dividend<0 and divisor>0) or (dividend>0 and divisor<0)):
            return (-ret)
        if (ret>=2**31-1):
            return 2**31-1
        if (ret<=-2**31):
            return -2**31
        return ret

c=Solution()
print(c.divide(1,1))