"""
669. Trim a Binary Search Tree
Medium

4352

231

Add to List

Share
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bstree import Node

class Solution:
    def trimBST(self, root: Node, low: int, high: int) -> Node:
        newroot = None
        while root.val > high:
            root = root.left
        newroot = root
        print (newroot.preorder())

S = Solution()
n = Node(16)
lst = [8,4,2,1,3,6,5,7,12,10,9,11,14,13,15,24,20,18,17,19,23,21,22,30,28,26,25,27,29,31]
for m in lst:
    n.insert(m)

n.preorder()
print ("\n")
n.inorder()
print ("\n")
S.trimBST(n,5,17)
    

        