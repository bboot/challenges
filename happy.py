#!/usr/bin/python

class Solution(object):
    def get_digits(self, n):
        if n == 0:
            return [0]
        x = []
        while n > 0:
            if n >= 10:
                x+=[n % 10]
            else:
                x.append(n)
		return x
            n = n/10
            print n
        return x

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = self.get_digits(n)
        while len(x):
            x = map(lambda x: x*x, x)
            n = 0
            for z in x:
                n = n+z
            x = self.get_digits(n)
        return True

s = Solution()
print s.isHappy(19)
