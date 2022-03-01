class Solution(object):
    ret = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rlen = len(obstacleGrid)
        clen = len(obstacleGrid[0])
        if not rlen or not clen:
            return 0
        ret = []
        for i in range(rlen):
            ret.append([0]*clen)
        for i in range(clen):
            if obstacleGrid[0][i] == 1:
                break
            else:
                ret[0][i] = 1
        for i in range(rlen):
            if obstacleGrid[i][0] == 1:
                break
            else:
                ret[i][0] = 1
        for i in range(1, rlen):
            for j in range(1, clen):
                if obstacleGrid[i][j] == 0:
                    ret[i][j] = ret[i-1][j]+ret[i][j-1]
                else:
                    continue
        return ret[rlen-1][clen-1]


c = Solution()
print(c.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
