#!/usr/bin/env python

import collections
import itertools

class Solution(object):
    def groupStrings(self, strings):
        key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]

    def groupStrings1(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        l = {}
        for s in strings:
            r = ''
            for i in range(0, len(s)-1):
                r += str(ord(s[i+1]) - ord(s[i]))
            if r not in l.keys():
                l[r] = [s]
            else:
                l[r].append(s)
        return [v for v in l.values()]

s = Solution()
print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])


'''
a = "hello"
b = collections.defaultdict(list)
c = collections.defaultdict(list)
b[a] += a,
c[a] += a
print b
print c
'''
D = [[] for i in xrange(4)]
print D
