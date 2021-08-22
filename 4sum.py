class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                l,r=j+1,n-1
                remain=target-nums[i]-nums[j]
                while l<r and j<l and r<n:
                    temp=nums[l]+nums[r]
                    if temp>remain:
                        r-=1
                    elif temp<remain:
                        l+=1
                    else:
                        if [nums[i],nums[j],nums[l],nums[r]] not in ret:
                            ret.append([nums[i],nums[j],nums[l],nums[r]])
                        r-=1
                        l+=1
        return ret

c=Solution()
print(c.fourSum([1,0,-1,0,-2,2],0))