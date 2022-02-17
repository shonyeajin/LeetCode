class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        s = s.split(' ')
        for i, n in enumerate(s):
            if n != '':
                return len(n)
        return 0


c = Solution()
print(c.lengthOfLastWord(" "))
