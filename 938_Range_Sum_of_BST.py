'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''方法3参考了题解，利用了BST的特性；方法2使用的是全局变量；方法1使用了stack；方法1和方法2都没有用到BST的特性'''
'''BST的特性：若左子树不为空, 则左子树的所有结点都小于根节点; 若右子树不为空, 则右子树的所有结点都大于根节点'''
class Solution3:
    def rangeSumBST3(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0

        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

class Solution2:
    res = 0
    '''#2: using a global variate'''
    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        if root.val>=L and root.val<=R:
            self.res += root.val

        self.rangeSumBST(root.left, L, R)
        self.rangeSumBST(root.right, L, R)

        return self.res

    '''# 1: using stack'''
    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        if (not root):
            return 0

        total_node_values = 0
        stack = []
        stack.append(root)
        while (len(stack) != 0):
            node = stack.pop()
            if node.val >= L and node.val <= R:
                total_node_values += node.val

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return total_node_values