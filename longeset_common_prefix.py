class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref=""
        idx=len(strs)
        if idx==0:
            return pref
        if idx==1:
            return strs[0]
        for i in range(len(strs[0])):
            for j in range(1,idx):
                if i==len(strs[j]) or (i<len(strs[j]) and strs[0][i]!=strs[j][i]):
                    return pref
            pref+=strs[0][i]
        return pref


c=Solution()
print(c.longestCommonPrefix(["dog","racecar","car"]))