class Solution(object):

    def retIdx(self, order, c):
        for i in range(0,len(order)):
            if order[i]==c:
                return (i)
        else:
            return (-1)
    
    def customSortString(self, order, str):
        for i in range(0,len(str)):
            for j in range(i+1, len(str)):
                r1=self.retIdx(order,str[i])
                r2=self.retIdx(order,str[j])
                if r1!=-1 and r2!=-1 and r1 > r2:
                    newStr=str[:i]+str[j]+str[i+1:j]+str[i]+str[j+1:]
                    str=newStr
        return (str);

            
n=Solution()
str=n.customSortString("kqep","pekeq")
print(str)