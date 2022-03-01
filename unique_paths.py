class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        ret = [[1]*n]
        for i in range(m-1):
            ret.append([1]+[0]*(n-1))
        for i in range(1, m):
            for j in range(1, n):
                ret[i][j] = ret[i-1][j]+ret[i][j-1]
        return ret[m-1][n-1]


c = Solution()
print(c.uniquePaths(3, 7))
