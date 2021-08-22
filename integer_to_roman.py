class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret=""
        while int(num/1000)>0:
            num-=1000
            ret+="M"
        if int(num/900)==1:
            num-=900
            ret+="CM"
        if int(num/500)==1:
            num-=500
            ret+="D"
        if int(num/400)==1:
            num-=400
            ret+="CD"
        while int(num/100)>0:
            num-=100
            ret+="C"
        if int(num/90)==1:
            num-=90
            ret+="XC"
        if int(num/50)==1:
            num-=50
            ret+="L"
        if int(num/40)==1:
            num-=40
            ret+="XL"
        while int(num/10)>0:
            num-=10
            ret+="X"
        if int(num/9)==1:
            num-=9
            ret+="IX"
        if int(num/5)==1:
            num-=5
            ret+="V"
        if int(num/4)==1:
            num-=4
            ret+="IV"
        while int(num/1)>0:
            num-=1
            ret+="I"
        return ret

c=Solution()
print(c.intToRoman(1994))