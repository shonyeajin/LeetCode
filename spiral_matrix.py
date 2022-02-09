class Solution(object):
    def move_r(self, matrix, curr, count, ret):
        if count[0] <= 0 or count[1] <= 0:
            return
        curr_h, curr_w = curr[0], curr[1]
        count_h, count_w = count[0], count[1]
        for i in range(count_w):
            curr_w += 1
            ret.append(matrix[curr_h][curr_w])
        count_h -= 1
        self.move_d(matrix, (curr_h, curr_w), (count_h, count_w), ret)

    def move_d(self, matrix, curr, count, ret):
        if count[0] <= 0 or count[1] <= 0:
            return
        curr_h, curr_w = curr[0], curr[1]
        count_h, count_w = count[0], count[1]
        for i in range(count_h):
            curr_h += 1
            ret.append(matrix[curr_h][curr_w])
        count_w -= 1
        self.move_l(matrix, (curr_h, curr_w), (count_h, count_w), ret)

    def move_l(self, matrix, curr, count, ret):
        if count[0] <= 0 or count[1] <= 0:
            return
        curr_h, curr_w = curr[0], curr[1]
        count_h, count_w = count[0], count[1]
        for i in range(count_w):
            curr_w -= 1
            ret.append(matrix[curr_h][curr_w])
        count_h -= 1
        self.move_u(matrix, (curr_h, curr_w), (count_h, count_w), ret)

    def move_u(self, matrix, curr, count, ret):
        if count[0] <= 0 or count[1] <= 0:
            return
        curr_h, curr_w = curr[0], curr[1]
        count_h, count_w = count[0], count[1]
        for i in range(count_h):
            curr_h -= 1
            ret.append(matrix[curr_h][curr_w])
        count_w -= 1
        self.move_r(matrix, (curr_h, curr_w), (count_h, count_w), ret)

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        h = len(matrix)
        w = len(matrix[0])
        ret = []

        self.move_r(matrix, (0, -1), (h, w), ret)
        return ret


c = Solution()
print(c.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
