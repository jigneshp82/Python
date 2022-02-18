"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""

import re
from typing import Optional
from bstree import Node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if root:
            r = 1 + self.maxDepth(root.right) 
            l = 1 + self.maxDepth(root.left)
        else:
            return 0
        return max(r,l)
        
        def findheight(root, right, left)->int:
            if root.left:
                left +=1
                findheight(root.left, right, left)
            if root.right:
                right+=1
                findheight(root.right,right, left)
            return max(right,left)
        
        return findheight(root,right, left)

s = Solution()
n = Node(10)
n.insert(3)
n.insert(9)
n.insert(20)
n.insert(15)
n.insert(7)
n.preorder()
print(s.maxDepth(n))
