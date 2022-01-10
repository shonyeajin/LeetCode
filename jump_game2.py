class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 현재 인덱스에서 마지막 인덱스까지 jump 부족하면 슬라이딩 윈도우 기법으로 max 값인 곳으로 jump
        # 충분하면 해결
        length = len(nums)
        cur = 0
        ret = 0
        while cur < length-1:
            jump = nums[cur]
            if cur+jump < length-1:
                print('a', cur, jump)
                #temp = nums[cur+1:cur+jump+1]
                temp = []
                for i in range(cur+1, cur+jump+1):
                    temp.append(nums[i]+i)
                idx = list(reversed(temp)).index(max(temp))
                cur = cur+jump-idx
                ret += 1
            else:
                print('b', cur)
                return ret+1
        return ret


c = Solution()
print(c.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
