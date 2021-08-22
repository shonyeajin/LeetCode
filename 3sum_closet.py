class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret=nums[0]+nums[1]+nums[2]
        i,j=0,len(nums)-1
        while i<j:
            k,j=i+1,len(nums)-1
            while k<j:
                temp=nums[i]+nums[j]+nums[k]
                if temp-target>0:
                    j-=1
                elif temp-target<0:
                    k+=1
                else:
                    return target
                if abs(temp-target)< abs(ret-target):
                    ret=temp
            i+=1
        return ret

c=Solution()
print(c.threeSumClosest([0,0,0],1))