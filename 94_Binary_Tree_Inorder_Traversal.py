'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        '''# 2: iterate version'''
        if not root:
            return []

        stack, res = [], []
        pCur = root
        while pCur or stack:  #根节点不为空，则入栈，同时将指针指向左子树，为下一次入栈左子树做准备
            if pCur:
                stack.append(pCur)
                pCur = pCur.left
            else:             #根节点为空，则出栈最后一个左树，并将该左树的右子树入栈，为下一次入栈该右子树的左子树做准备
                node = stack.pop()
                res.append(node.val)
                pCur = node.right

        return res

    '''# 1: recursion version'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)