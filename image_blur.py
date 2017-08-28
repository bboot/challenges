#!/usr/bin/env python

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        nc = len(M[0])
        nr = len(M)
        res = [[0 for i in xrange(nc)] for j in xrange(nr)]
        bounds = [-1, 0, 1]
        for c in xrange(nc):
            for r in xrange(nr):
                sm = 0
                cnt = 0
                for bc in bounds:
                    tc = c + bc
                    for br in bounds:
                        tr = r + br
                        if tc < 0 or tc >= nc or tr < 0 or tr >= nr:
                            continue
                        cnt += 1
                        sm += M[tr][tc]
                res[r][c] = int(sm / cnt)
        return res

im = [[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]]
s = Solution()
print s.imageSmoother(im)
