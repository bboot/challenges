#!/usr/bin/env python

'''
Trees in the following code are specified in BFS order

(from http://www.geeksforgeeks.org/?p=618)
Example: [1,2,3,4,5,None,None]
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5
'''

import math
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Tree:
    def __init__(self, vec):
        self.vector = vec
        lvls = self.create_levels(vec)
        level1 = self.attach_levels(lvls)
        self.root = level1[0]

    def height(self):
        def height(hmax, level, p):
            if not p or p == '@':
                return 0
            hmax = max(hmax, level)
            hmax = max(hmax, height(hmax, level+1, p.left))
            hmax = max(hmax, height(hmax, level+1, p.right))
            return hmax
        hmax = height(1, 1, self.root)
        return hmax

    def is_node(self, p):
        if not p or p == '@':
            return False
        return True

    def preOrderNoRecursion(self):
        rights = []
        def push(p):
            if self.is_node(p):
                rights.append(p)

        def pop():
            if rights:
                return rights.pop()

        pre_order = []
        p = self.root
        while self.is_node(p):
            pre_order.append(p.val)
            # remember the right node, if any
            push(p.right)
            # get next left
            p = p.left
            if not self.is_node(p):
                # no left, so check last recorded right node
                p = pop()
        return pre_order

    def preOrderTraversal(self):
        ''' uses Recursion '''
        pre_order = []
        def preOrderTraversal(vals, p):
            if not self.is_node(p):
                return '@'
            vals.append(p.val)
            preOrderTraversal(vals, p.left)
            preOrderTraversal(vals, p.right)
        preOrderTraversal(pre_order, self.root)
        return pre_order

    def inOrderNoRecursion(self):
        queue = []
        def push(p):
            if self.is_node(p):
                queue.append(p)
        def pop():
            if queue:
                return queue.pop()
            return '*'

        in_order = []
        p = self.root
        while self.is_node(p):
            push(p)
            p = p.left
            while not self.is_node(p):
                p = pop()
                if p == '*':
                    # we have completed the traversal
                    return in_order
                in_order.append(p.val)
                p = p.right
        return in_order

    def inOrderTraversal(self):
        ''' uses Recursion '''
        in_order = []
        def inOrderTraversal(vals, p):
            if not self.is_node(p):
                return '@'
            inOrderTraversal(vals, p.left)
            if p.val != '@':
                vals.append(p.val)
            inOrderTraversal(vals, p.right)
        inOrderTraversal(in_order, self.root)
        return in_order

    def postOrderNoRecursion(self):
        queue = []
        def push(p, is_right):
            if self.is_node(p):
                #print "push", p.val, is_right
                queue.append((p, is_right))
        def pop():
            if queue:
                p, r = queue.pop()
                #print "pop", p.val, r
                return p,r

        post_order = []
        p = self.root
        # bias means "when I get popped from the {right|left}"
        bias = False # left
        while self.is_node(p):
            push(p, bias)
            p = p.left
            bias = False
            while not self.is_node(p) or bias:
                if not queue:
                    return post_order
                p = queue[-1][0].right
                bias = True
                if not self.is_node(p):
                    p, new_bias = pop()
                    post_order.append(p.val)
                    while new_bias:
                        p, new_bias = pop()
                        post_order.append(p.val)
                    continue
                break
        return post_order

    def postOrderTraversal(self):
        ''' uses Recursion '''
        post_order = []
        def postOrderTraversal(vals, p):
            if not self.is_node(p):
                return '@'
            val = postOrderTraversal(vals, p.left)
            if val != '@':
                vals.append(val)
            val = postOrderTraversal(vals, p.right)
            if val != '@':
                vals.append(val)
            return p.val
        val = postOrderTraversal(post_order, self.root)
        if val != '@':
            post_order.append(val)
        return post_order

    def create_levels(self, vec):
        ''' create all the nodes, but the vertices are not '''
        ''' attached '''
        L = len(vec)
        levels = int(math.log(L, 2))
        lvls = [[] for x in range(0, levels+1)]
        for lv in reversed(range(1, levels+1)):
            L = L-2**lv
            l = vec[L:]
            for n in l:
                t = ['@']
                if n is not None:
                    t = [TreeNode(n, None, None)]
                lvls[lv] += t
            vec = vec[:L]
        lvls[0] = [TreeNode(vec[0], None, None)]

        return lvls

    def attach_levels(self, lvls):
        ''' attach all the vertices '''
        ''' ivalue: list of nodes for each level (list of lists) '''
        '''    first index is level, second index is node in that level '''
        ''' rvalue: root TreeNode '''
        nlevels = len(lvls)
        for lv in range(0, nlevels - 1):
            ''' len(lvls[lv] is 2**lv '''
            for k in range(0, len(lvls[lv])):
                j = 2*k
                if lvls[lv][k] != '@':
                    lvls[lv][k].left = lvls[lv+1][j]
                    lvls[lv][k].right = lvls[lv+1][j+1]
        return lvls[0]

class Solution(object):
    def __init__(self):
        self.mins = {}
        self.maxs = {}

    def dfs(self, node, level, num):
        if (node == None or node == '@'):
            return
        if level in self.mins.keys():
            self.mins[level] = min(self.mins[level], num)
        else:
            self.mins[level] = num
        if level in self.maxs.keys():
            self.maxs[level] = max(self.maxs[level], num)
        else:
            self.maxs[level] = num
        self.dfs(node.left, level + 1, 2*num)
        self.dfs(node.right, level + 1, 2*num+1)

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 1, 1)
        m = 0
        for level in self.mins.keys():
            if level in self.maxs.keys():
                m = max(m, self.maxs[level] - self.mins[level] + 1)
        return m

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        leaves = []
        def dfs(node, s):
            if node == None or node == '@':
                return 0
            s += node.val
            left = dfs(node.left, s)
            right = dfs(node.right, s)
            if left == 0 and right == 0:
                leaves.append(s)
                return s
            return left + right
        s = 0
        dfs(root, s)
        if sum in leaves:
            return True
        return False

def compare(a, b):
    c = [i for i, j in zip(a, b) if i != j]
    if c:
        print "FAIL",c
    return c

def main(tests):
    #for config in tests[-1:0:-1]:
    for config in tests:
        t = Tree(config)
        print "*****", config
        rec = t.preOrderTraversal()
        norec = t.preOrderNoRecursion()
        print "pre order:", rec
        print "pre order no recursion:", norec
        compare(rec, norec)
        rec = t.inOrderTraversal()
        norec = t.inOrderNoRecursion()
        print "in order:", rec
        print "in order no recursion:", norec
        compare(rec, norec)
        rec = t.postOrderTraversal()
        norec = t.postOrderNoRecursion()
        print "post order:", rec
        print "post order no recursion:", norec
        compare(rec, norec)
        s = Solution()
        print "width:", s.widthOfBinaryTree(t.root)
        print "height:", t.height()

if __name__=="__main__":
    tests = [[5,4,8,11,None,13,4,7,2,None,None,None,None,None,1],
             [1],
             [1,3,2,5,3,None,9],
             [1,3,None,5,3,None,None],
             [1,3,2,5,None,None,None],
             [1,3,2,5,None,None,9,6,None,None,None,None,None,None,7],
             [1,2,3,4,5,None,None],]
    #sys.exit(main(tests))
    print "+++++++++++++++++++++++++++++++++++++++++++++++ hasPathSum"
    test = tests[0]
    sum = 22
    #test = tests[1]
    #sum = 1
    print "*****", test
    t = Tree(test)
    s = Solution()
    print s.hasPathSum(t.root, sum)

