'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''迭代法和前序遍历法'''
class Solution:
    def isSameTree4(self, p: TreeNode, q: TreeNode) -> bool:
        # 4: 后序遍历，左右根，双栈实现
        if (p == None) and (q == None): return True
        if (p == None) or (q == None): return False

        stackp, stackpTmp = [], []
        stackq, stackqTmp = [], []
        while (p != None) or (q != None) or (len(stackpTmp) != 0) or (len(stackqTmp) != 0):
            if (p != None) and (q != None):
                stackp.append(p)
                stackpTmp.append(p)
                stackq.append(q)
                stackqTmp.append(q)
                p = p.right
                q = q.right
            elif (p == None) and (q == None):
                p = stackpTmp.pop()
                p = p.left
                q = stackqTmp.pop()
                q = q.left
            else:
                return False

        while (len(stackp) != 0) and (len(stackq) != 0):
            if (stackp.pop().val != stackq.pop().val):
                return False

        return True

    '''# 3: none recursion version, 中序遍历，左根右'''
    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
        if (p==None) and (q==None): return True
        if (p==None) or (q==None): return False
        stackp, stackq = [], []

        while (p != None) or (q != None) or (len(stackp) != 0) or (len(stackq) != 0):
            if (p != None) and (q != None):
                stackp.append(p)
                stackq.append(q)
                p = p.left
                q = q.left
            elif (p==None) and (q==None):
                p = stackp.pop()
                q = stackq.pop()
                if (p.val != q.val):
                    return False
                p = p.right
                q = q.right
            else:
                return False

        return True

    '''#2: none recursion version, 前序遍历'''
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if (p==None) and (q==None): return True
        if (p==None) or (q==None): return False
        stackp, stackq = [], []
        stackp.append(p)
        stackq.append(q)

        while (len(stackp) != 0) or (len(stackq) != 0):
            pNode, qNode = stackp.pop(), stackq.pop()
            if (pNode==None) and (qNode==None): continue
            if (pNode==None) or (qNode==None): return False
            if (pNode.val != qNode.val):
                return False
            else:
                stackp.append(pNode.right)
                stackq.append(qNode.right)
                stackp.append(pNode.left)
                stackq.append(qNode.left)

        return True

    '''#1: recursion version'''
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        #根节点都为空，则为同一个树
        if (p == None) and (q == None): return True
        #一个根节点为空，另外一个不为空，不是同一个树
        if p == None or q == None: return False

        #根节点非空，但其值不同，则也不是同一颗树
        if q.val != p.val: return False

        #根节点比较完了，分别比较左右节点
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)