class Solution(object):
    def dfs(self, nums, ret, curr):
        if len(nums) == 0:
            ret.append(curr)
            return
        for i, c in enumerate(nums):
            self.dfs(nums[:i]+nums[i+1:], ret, curr+[c])

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(nums, ret, [])
        ret = list(set(list(map(tuple, ret))))
        return ret


c = Solution()
print(c.permuteUnique([1, 1, 2]))
