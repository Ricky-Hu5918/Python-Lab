'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric2(self, root: TreeNode) -> bool:
        '''# 2: recursion version'''
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)

    '''# 1: iterate version'''
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root: return True

        #每一层的节点值都是一个回文串，则该tree是对称的
        queue = collections.deque()
        queue.append(root)
        while (len(queue) != 0 ):
            level_value_list = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_value_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_value_list.append(None)
            if level_value_list != level_value_list[::-1]:
                return False

        return True
