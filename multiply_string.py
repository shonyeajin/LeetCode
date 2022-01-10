class Solution(object):
    def my_atoi(self, s):
        ret = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        for i, c in enumerate(s):
            ret = ret*10 + ord(c)-48
        return ret*sign

    def my_itoa(self, num):
        sign = 0
        ret = ""
        l = "0123456789"
        if num < 0:
            num *= -1
            sign = 1
        while num//10 != 0:
            ret = l[int(num % 10)]+ret
            num = num//10

        ret = l[int(num % 10)]+ret
        if sign:
            ret = '-'+ret
        return ret

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # atoi로 바꿈
        # itoa로 바꿈
        n1 = self.my_atoi(num1)
        n2 = self.my_atoi(num2)
        return self.my_itoa(n1*n2)


c = Solution()
c.multiply("1", "-2")
