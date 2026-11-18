# LC 236 Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(node, p, q):
            if not node:
                return node
            left = postorder(node.left, p, q)
            right = postorder(node.right, p, q)

            if left and right:
                return node
            elif node == p or node == q:
                return node
            elif left and not right:
                return left
            elif right and not left:
                return right
            else:
                return None
        return postorder(root, p, q)
