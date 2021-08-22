class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        ret=0
        if x<0:
            sign=-1
            x*=(-1)
        while x!=0:
            ret=ret*10+x%10
            x=int(x/10)
        ret*=sign
        if ret < -2**31 or ret>2**31-1:
            return 0
        return (ret)

c=Solution()
print(c.reverse(1534236469))