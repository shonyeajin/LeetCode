class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))]+list(zip(*A[::-1]))
            print('lo:{}, hi:{}, A:{}'.format(lo, hi, A))
        return A


c = Solution()
print(c.generateMatrix(3))
