#!/usr/bin/env python

'''
'''

class Solution(object):
    ''' leetcode runtime: 55 ms '''
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [None for i in xrange(32)]
        for n in nums:
            t = n % 100
            v = n % 10
            p = (t - v) / 10
            d = (n - t) / 100
            a[2**(d-1)-1 + (p-1)] = v
        def dfs(i, s):
            if a[i] == None:
                return 0
            s += a[i]
            l = dfs(2*i + 1, s)
            r = dfs(2*i + 2, s)
            if l == 0 and r == 0:
                return s
            return l + r
        s = dfs(0, 0)
        return s

tests = [[113, 215, 221],
         [111, 212, 223, 314, 325, 336, 347],
         [111,217,221,315,415],
         [113,229,349,470,485],
        ]
for t in tests:
    s = Solution()
    print t
    print s.pathSum(t)
