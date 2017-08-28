#!/usr/bin/env python

import heapq
import itertools

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        print streams
        stream = heapq.merge(*streams)
        print stream
        return [suv[1:] for suv in itertools.islice(stream, k)]

s = Solution()
#s.kSmallestPairs([1,1,2],[1,2,3],2)
s.kSmallestPairs([1,],[1,5,8],2)
