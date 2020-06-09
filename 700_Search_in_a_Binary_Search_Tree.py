'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        # 2: recursion
        if root == None: return root

        if root.val == val:
            return root

        return self.searchBST(root.left, val) or self.searchBST(root.right, val)

    '''# 1: iterate'''
    def searchBST1(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return root

        stackTmp = []
        stackTmp.append(root)
        while len(stackTmp) != 0:
            node = stackTmp.pop()
            if node:
                if node.val == val:
                    return node
                else:
                    stackTmp.append(node.right)
                    stackTmp.append(node.left)

        return None