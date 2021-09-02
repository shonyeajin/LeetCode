class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =="":
            return 0
        elif haystack=="":
            return -1
        needle_length=len(needle)
        haystack_length=len(haystack)
        i=0
        while i<haystack_length and i+needle_length<=haystack_length:
            if haystack[i:i+needle_length]==needle:
                return i
            i+=1
        return -1
c=Solution()
print(c.strStr("hello","ll"))
        
