class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        ret=[""]
        numDict={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

        for i in range(len(digits)):
            temp=[]
            for j in range(len(ret)) :
                for k in range(len(numDict[int(digits[i])])):
                    temp.append(ret[j]+numDict[int(digits[i])][k])
            ret=temp
        return ret
                

c=Solution()
print(c.letterCombinations("2"))

