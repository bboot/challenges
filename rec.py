class Solution(object):
    def get_area(self, x):
        return (x[3]-x[1])*(x[2]-x[0])

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        As = 0
        for x in rectangles:
            As += self.get_area(x)

        ll = [[x[0],x[1]] for x in rectangles]
        ll.sort(key=lambda x: x[0]+x[1])
        ll = ll[0]

        ur = [[x[2],x[3]] for x in rectangles]
        ur.sort(key=lambda x: x[0]+x[1], reverse=True)
        ur = ur[0]

        At = self.get_area(ll + ur)
        if At != As:
            return False

        # Now need to check overlap
        for i in range(0, 4):
            for x in rectangles[i:-1]:
                # get rec with biggest x|y
                # 1. get its smallest x|y
                # 2. subtract the biggest x|y of the complement rec
                # 3. should be >= 0
                pass
        return True

[[0,0,1,1],[0,1,3,2],[1,0,2,2]]
