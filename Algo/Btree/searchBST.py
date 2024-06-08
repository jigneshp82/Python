"""
700. Search in a Binary Search Tree
Easy

3082

146

Add to List

Share
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from bstree import Node
class Solution:
    def searchBST(self, root: Optional[Node], val: int) -> Optional[Node]:

        if root.val == val:
            return root
        elif root.val < val:
            if root.left : return self.searchBST(root.left, val)
        elif root.val > val:
            if root.right: return self.searchBST(root.right, val)
        return None
        
        