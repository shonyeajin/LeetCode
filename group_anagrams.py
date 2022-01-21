class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s = dict()
        ret = []
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in s:
                s[temp] = [strs[i]]
            else:
                s[temp].append(strs[i])

        return list(s.values())


c = Solution()
print(c.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
