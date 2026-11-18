# LC 106 Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        def build(inorder,postorder):
            if not postorder:
                return None
            mid = postorder[-1]
            mid_pos = inorder.index(mid)
            node = TreeNode(val=mid)
            
            left_inorder = inorder[:mid_pos]
            left_size = len(left_inorder)
            left_postorder = postorder[:left_size]
            right_inorder = inorder[mid_pos+1:]
            right_postorder = postorder[left_size:-1]
            lefttree = build(left_inorder,left_postorder)
            righttree = build(right_inorder,right_postorder)
            node.left = lefttree
            node.right = righttree
            return node
        return build(inorder,postorder)
