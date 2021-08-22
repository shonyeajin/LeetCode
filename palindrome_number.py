class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        for i in range(int(len(s)/2)):
            if s[i]!=s[-i-1]:
                return False
        return True
        
c=Solution()
print(c.isPalindrome(-101))
