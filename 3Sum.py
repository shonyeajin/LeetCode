class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i,j=0, len(nums)-1
        result=[]
        while i<j:
            k,j=i+1,len(nums)-1
            while k<j:
                temp=nums[i]+nums[j]+nums[k]
                if temp>0:
                    j-=1
                elif temp<0:
                    k+=1
                else:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    k+=1
            i+=1
        return result


c=Solution()
print(c.threeSum([-1,0,1,2,-1,-4]))        