class Solution(object):
    def listToInt(self, arr):
        ret=0
        for i in range(len(arr)):
            ret=ret*10+arr[i]
        return ret

    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        leng=len(arr)
        for i in range(leng-1):
            part1=self.listToInt(arr[:i+1])
            for j in range(i+2, leng):
                if part1 == self.listToInt(arr[i+1:j]) and part1==self.listToInt(arr[j:]):
                    print("part1:{},part2:{},part3:{}".format(part1,self.listToInt(arr[i+1:j]),self.listToInt(arr[j:])))
                    return [i,j]
        return [-1,-1]
c=Solution()
print(c.threeEqualParts([1,1,0,1,1]))
                
