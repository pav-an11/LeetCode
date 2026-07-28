class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        reverse = int(str(abs(x))[::-1])
        result = sign * reverse

        if result < -2147483648 or result > 2147483647:
            return 0
        else:
            return result

        