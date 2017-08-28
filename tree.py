# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def width(self, root, level):
        for i in level:
            cnt = 0
            node = root[i]
            left = root[i+1]
            right = root[i+2]
            if left != None or right != None:
                cnt += 2
            cnts += cnt
        return cnts
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        w = 0
        if root.left != None or root.right != None:
            w += 2
