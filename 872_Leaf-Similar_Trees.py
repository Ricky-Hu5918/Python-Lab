'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:
Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''利用中序遍历的思路（LDR），但只有当出栈节点的左右子树都为空时，才将该节点的val保存起来。'''
class Solution:
    def leafSimilar1(self, root1: TreeNode, root2: TreeNode) -> bool:
        def collect_leaves(root):
            stack, res = [], []
            pCur = root
            while pCur or stack:
                if pCur:
                    stack.append(pCur)
                    pCur = pCur.left
                else:
                    node = stack.pop()
                    if not node.left and not node.right:
                        res.append(node.val)
                    pCur = node.right

            return res

        return collect_leaves(root1) == collect_leaves(root2)

    '''# 2: 深度搜索, yield生成器的用法'''
    def leafSimilar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val

                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

root1, root2 = [3,5,1,6,2,9,8,null,null,7,4], [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]