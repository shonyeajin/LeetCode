class Solution(object):
    def factorial(self, n):
        ret = 1
        for i in range(1, n+1):
            ret *= i
        return ret

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # n = 3
        ret = ""
        s = list(range(1, n+1))
        for i in range(n-1):
            fac = self.factorial(n-1-i)
            ret = ret+str(s[(k-1)//fac])
            # print('i:{}, fac:{}, k:{}, ret:{}, s:{}'.format(
            #    i, fac, k, ret, s))
            del s[(k-1)//fac]
            k = k % fac
        ret += str(s[0])
        return ret


c = Solution()
print(c.getPermutation(3, 1))
