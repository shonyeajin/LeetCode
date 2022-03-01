class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rlen = len(grid)
        clen = len(grid[0])
        ret = []
        for i in range(rlen):
            ret.append([0]*clen)
        ret[0][0] = grid[0][0]
        for i in range(1, rlen):
            ret[i][0] = ret[i-1][0]+grid[i][0]
        for i in range(1, clen):
            ret[0][i] = ret[0][i-1]+grid[0][i]
        for i in range(1, rlen):
            for j in range(1, clen):
                ret[i][j] = min(ret[i-1][j], ret[i][j-1])+grid[i][j]
        return ret[rlen-1][clen-1]


c = Solution()
print(c.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
