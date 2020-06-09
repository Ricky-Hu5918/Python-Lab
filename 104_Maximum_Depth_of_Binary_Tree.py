'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

'''求二叉树深度的解法'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''# 3: DFS深度优先搜素，利用递归的栈，借助level标记当前层'''
    def maxDepth3(self, root: TreeNode) -> int:
        if not root: return 0
        self.depth = 0
        self._dfs(root, 0)
        return self.depth

    def _dfs(self, node, level):
        if not node: return
        if self.depth < level + 1:
            self.depth = level + 1

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)

    '''# 2: BFS广度优先搜索，使用双端队列deque'''
    def maxDepth2(self, root: TreeNode) -> int:
        if not root: return 0

        queue = collections.deque()
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth

    '''# 1: DFS+分治'''
    def maxDepth1(self, root: TreeNode) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1