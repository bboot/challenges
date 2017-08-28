class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        leaves = []
        def dfs(node, sum):
            if node == None:
                return 0
            sum += node.val
	    print sum
            left = dfs(node.left, sum)
            right = dfs(node.right, sum)
            if left == 0 and right == 0:
                leaves.append(sum)
                return sum
            return left + right
        sum = 0
        dfs(root, sum)
        if 22 in leaves:
            return True
        return False

s = Solution()
sum = 0
print s.hasPathSum(root, sum)
