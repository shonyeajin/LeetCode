class Solution(object):
    def midCul(self, s, i, numRows, sLen):
        ret=""
        offset1 = 2*(numRows-i-1)
        offset2 = 2*i
        flag=0
        j=i
        while j<sLen:
            if flag==0:
                ret+=s[j]
                j+=offset1
                flag=1
            else:
                ret+=s[j]
                j+=offset2
                flag=0
        return ret

    def endCul(self, s, i, numRows, sLen):
        ret=""
        offset=2*numRows-3+1
        for j in range(i, sLen, offset):
            ret+=s[j]
        return ret

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret=""
        sLen=len(s)
        if numRows==1:
            return s
        for i in range(numRows):
            if i%numRows==0 or i%numRows==numRows-1:
                ret+=self.endCul(s, i, numRows, sLen)
            else:
                ret+=self.midCul(s,i, numRows, sLen)
        return ret

c=Solution()
print(c.convert("PAYPALISHIRING",1))