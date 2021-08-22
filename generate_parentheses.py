class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(curr, opened, closed, length, n):
            if length == n*2:
                res.append(curr)
                return
            elif opened == closed:
                dfs(curr+'(', opened+1, closed, length+1, n)
            elif opened > closed and opened == n:
                dfs(curr+')', opened, closed+1, length+1, n)
            elif opened > closed and opened < n:
                dfs(curr+'(', opened+1, closed, length+1, n)
                dfs(curr+')', opened, closed+1, length+1, n)

        dfs('', 0, 0, 0, n)
        return res


c = Solution()
print(c.generateParenthesis(3))
