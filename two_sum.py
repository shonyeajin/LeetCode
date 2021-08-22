class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    retList=[]
                    retList.append(i)
                    retList.append(j)
                    return (retList)

                    