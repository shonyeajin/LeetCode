class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=i=0
        leng=len(s)
        while i<leng and s[i]=='M':
            ret+=1000
            i+=1
        if i+1<leng and s[i:i+2]=="CM":
            ret+=900
            i+=2
        if i<leng and s[i]=='D':
            ret+=500
            i+=1
        if i+1<leng and s[i:i+2]=="CD":
            ret+=400
            i+=2
        while i<leng and s[i]=='C':
            ret+=100
            i+=1
        if i+1<leng and s[i:i+2]=="XC":
            ret+=90
            i+=2
        if i<leng and s[i]=='L':
            ret+=50
            i+=1
        if i+1<leng and s[i:i+2]=="XL":
            ret+=40
            i+=2
        while i<leng and s[i]=='X':
            ret+=10
            i+=1
        if i+1<leng and s[i:i+2]=="IX":
            ret+=9
            i+=2
        if i<leng and s[i]=='V':
            ret+=5
            i+=1
        if i+1<leng and s[i:i+2]=="IV":
            ret+=4
            i+=2
        while i<leng and s[i]=='I':
            ret+=1
            i+=1
        return (ret)

c=Solution()
print(c.romanToInt("MCMXCIV"))